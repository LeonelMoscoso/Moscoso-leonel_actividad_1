import json
import os


class Ingestiones:
    def __init__(self):
        self.ruta_static = "src/pad/static/"

    def leer_json(self):
        """Lee un archivo JSON y lo devuelve como un diccionario"""
        ruta_json = os.path.join(self.ruta_static, "json/datos.json")
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                datos = json.load(f)
            return datos
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_json}")
            return {}
        except json.JSONDecodeError:
            print(f"Error: El archivo {ruta_json} no es un JSON válido")
            return {}

    def leer_txt(self):
        """Lee un archivo de texto y lo devuelve como una cadena"""
        ruta_txt = os.path.join(self.ruta_static, "txt/info.txt")
        try:
            with open(ruta_txt, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_txt}")
            return ""

    def leer_varios_txt(self, nombre=""):
        """Lee cualquier archivo de texto dentro de /txt/"""
        ruta_txt = os.path.join(self.ruta_static, "txt", nombre)
        try:
            with open(ruta_txt, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_txt}")
            return ""

    def leer_cualquier_excel(self, nombre=""):
        """Lee un archivo Excel (por implementar)"""
        pass

    def leer_cualquier_csv(self, nombre=""):
        """Lee un archivo CSV (por implementar)"""
        pass

    def leer_html(self, url=""):
        """Lee HTML desde una URL (por implementar)"""
        pass

    def leer_bd(self, nombre_bd="", servidor="", puerto=0):
        """Lee datos desde una base de datos (por implementar)"""
        pass

    def leer_api(self, url=""):
        """Consume datos de una API (por implementar)"""
        pass

    def escribir_json(self, datos, nombre="datos_salida.json"):
        """Escribe un diccionario en un archivo JSON"""
        ruta_json = os.path.join(self.ruta_static, "json", nombre)
        try:
            with open(ruta_json, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            print(f"Archivo JSON guardado en: {ruta_json}")
        except Exception as e:
            print(f"Error al escribir JSON: {e}")

    def escribir_txt(self, nombre, datos):
        """Escribe datos en un archivo de texto"""
        ruta_txt = os.path.join(self.ruta_static, "txt", f"{nombre}.txt")
        try:
            with open(ruta_txt, "w", encoding="utf-8") as f:
                if isinstance(datos, list):
                    f.writelines("\n".join(datos))
                else:
                    f.write(str(datos))
            print(f"Archivo guardado en: {ruta_txt}")
        except Exception as e:
            print(f"Error al escribir TXT: {e}")


# Crear instancia de la clase
inges = Ingestiones()

# Leer JSON
datos_json = inges.leer_json()
print(datos_json)

print("************************************************************")

# Leer TXT
datos_txt = inges.leer_txt()
print(datos_txt)

print("************************************************************")

# Leer otro archivo TXT
nombre_archivo = "info copy.txt"
datos_txt_dos = inges.leer_varios_txt(nombre_archivo)
print(datos_txt_dos)

print("************************************************************")

# Guardar archivos TXT
inges.escribir_txt(nombre="archivo_json", datos=json.dumps(datos_json, indent=4, ensure_ascii=False))
inges.escribir_txt(nombre="archivo_txt", datos=datos_txt)
inges.escribir_txt(nombre="archivo_txt_copy", datos=datos_txt_dos)
