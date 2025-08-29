import csv
import sys
from django.db import transaction
from django.core.exceptions import ValidationError
from oficina.models import Oficina

def run(*args):
    if not args:
        print("Error: Favor de proporcionar la ruta del archivo")
        print("Uso: python manage.py runscript importar_oficina <ruta_del_archivo>")
        sys.exit(1)

    csv_file= args[0]
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            oficinas_a_crear = []
            
            for row in reader:
                nombre = row.get('nombre')
                nombre_corto = row.get('nombre_corto')

                if not nombre or not nombre_corto:
                    print(f"Error: Faltan datos en la fila: {row}. Falta un campo obligatorio.")
                    continue
                try:
                    oficina = Oficina(nombre=nombre, nombre_corto=nombre_corto)
                    oficina.full_clean()  # Validar el modelo
                    oficinas_a_crear.append(oficina)
                except ValidationError as e:
                    print(f"Error de validacion en la fila {row}. Detalle del error: {e}")
                except Exception as e:
                    print(f"Error inesperado en la fila {row}. Detalle del error: {e}")

            with transaction.atomic():
                Oficina.objects.bulk_create(oficinas_a_crear)
                print(f"Importacion de {len(oficinas_a_crear)} Oficinas creadas exitosamente.")
    except FileNotFoundError:
        print(f"Error: El archivo '{csv_file}' no fue encontrado.")
    except Exception as e:
        print(f"Error inesperado en la importacion: {e}")