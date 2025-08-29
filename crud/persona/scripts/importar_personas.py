import csv
import sys
from django.db import transaction
from django.core.exceptions import ValidationError
from oficina.models import Oficina
from persona.models import Persona

def run(*args):
    if not args:
        print("Error: Favor de proporcionar la ruta del archivo")
        print("Uso: python manage.py runscript importar_personas <ruta_del_archivo>")
        sys.exit(1)

    csv_file = args[0]

    oficinas_map = {oficina.nombre_corto: oficina for oficina in Oficina.objects.all()}

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            personas_a_crear = []
            
            for row in reader:
                nombre = row.get('nombre')
                edad = row.get('edad')
                email = row.get('email')
                oficina_nombre_corto = row.get('oficina_nombre_corto')

                if not nombre or not edad or not email or not oficina_nombre_corto:
                    print(f"Error en fila {row}. Falta el nombre o la edad")
                    continue
                try:
                    edad_int= int(edad)
                except (ValueError, TypeError):
                    print(f"Error en fila {row}. La edad no es un numero valido")
                    continue
                oficina_obj = None
                if oficina_nombre_corto:
                    oficina_obj = oficinas_map.get(oficina_nombre_corto)
                    if not oficina_obj:
                        print(f"Warning: No existe la oficina mencionada en la fila {row}")
                        print(f"Se creara el registro sin oficina")

                    try:
                        persona= Persona(nombre= nombre, edad=edad_int, email=email, oficina=oficina_obj)
                        persona.full_clean()  # Validar el modelo
                        personas_a_crear.append(persona)
                    except ValidationError as e:
                        print(f"Error de validacion en fila {row}. Detalle del error: {e}")
                    except Exception as e:
                        print(f"Error inesperado en fila {row}. Detalle del error: {e}")

            with transaction.atomic():
                Persona.objects.bulk_create(personas_a_crear)
                print(f"Importacion de {len(personas_a_crear)} Personas creadas exitosamente.")

    except FileNotFoundError:
        print(f"Error: El archivo '{csv_file}' no fue encontrado.")
    except Exception as e:
        print(f"Error inesperado en la importacion: {e}")
                    