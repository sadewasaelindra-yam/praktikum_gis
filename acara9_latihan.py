# ============================================
# Nama Lengkap : Sadewa Saelindra
# NIM          : 25/568929/SV/27564
# Tanggal      : 7 Mei 2026
# File         : acara9_latihan.py
# Deskripsi    : Latihan PyQGIS Console Acara 9
# ============================================

# -------------------------------
# Bagian 1: Pengenalan PyQGIS Console
# -------------------------------
print("Halo dari QGIS!")
print(Qgis.QGIS_VERSION)
print(type(iface))  # iface adalah objek global QGISInterface

# -------------------------------
# Bagian 2.1: QgsProject - proyek QGIS
# -------------------------------
project = QgsProject.instance()
print(f"File proyek: {project.fileName()}")

semua_layer = project.mapLayers()
print(f"Jumlah layer: {len(semua_layer)}")
for layer_id, layer in semua_layer.items():
    print(f" - {layer.name()} (tipe: {layer.type()})")

# -------------------------------
# Bagian 2.2: iface.activeLayer() - layer aktif
# -------------------------------
layer = iface.activeLayer()
if layer is None:
    print("Tidak ada layer yang dipilih di panel Layers.")
else:
    print(f"Layer aktif : {layer.name()}")
    print(f"Tipe geometri : {layer.geometryType()}")  # 0=Point,1=Line,2=Polygon
    print(f"Jumlah fitur : {layer.featureCount()}")
    print(f"CRS : {layer.crs().authid()}")

# -------------------------------
# Bagian 2.3: QgsVectorLayer - field & extent
# -------------------------------
fields = layer.fields()
print(f"Jumlah field: {fields.count()}")
for field in fields:
    print(f" - {field.name()} ({field.typeName()})")

ext = layer.extent()
print(f"xMin: {ext.xMinimum():.4f}, xMax: {ext.xMaximum():.4f}")
print(f"yMin: {ext.yMinimum():.4f}, yMax: {ext.yMaximum():.4f}")

# -------------------------------
# Bagian 3.1: Kontrol visibilitas layer
# -------------------------------
root = QgsProject.instance().layerTreeRoot()
node = root.findLayer(layer.id())
node.setItemVisibilityChecked(False)
print(f"Layer {layer.name()} disembunyikan")
node.setItemVisibilityChecked(True)
print(f"Layer {layer.name()} ditampilkan kembali")
print(f"Terlihat: {node.isVisible()}")

# -------------------------------
# Bagian 3.2: Ganti nama & opacity
# -------------------------------
nama_lama = layer.name()
layer.setName("Layer Hasil Edit")
print(f"Nama: {nama_lama} -> {layer.name()}")

layer.setOpacity(0.7)
iface.mapCanvas().refresh()
print(f"Opacity: {layer.opacity()}")

# Kembalikan ke semula
layer.setName(nama_lama)
layer.setOpacity(1.0)
iface.mapCanvas().refresh()

# -------------------------------
# Bagian 3.3: Zoom ke layer
# -------------------------------
iface.zoomToActiveLayer()
extent = layer.extent()
print(f"Extent: {extent.toString()}")

# -------------------------------
# Bagian 3.4: Berpindah ke layer lain
# -------------------------------
nama_target = "sungai_kab_bandung"  # ganti sesuai layer lain di proyekmu
hasil_pencarian = QgsProject.instance().mapLayersByName(nama_target)
if hasil_pencarian:
    layer_tujuan = hasil_pencarian[0]
    iface.setActiveLayer(layer_tujuan)
    print(f"Aktif sekarang: {iface.activeLayer().name()}")

# -------------------------------
# Bagian 4.1: Membaca symbology
# -------------------------------
renderer = layer.renderer()
print(f"Tipe renderer : {renderer.type()}")  # contoh: singleSymbol
symbol = renderer.symbol()
print(f"Tipe simbol : {symbol.type()}")  # 0=Marker,1=Line,2=Fill
for i, sl in enumerate(symbol.symbolLayers()):
    print(f" Symbol layer {i} : {sl.layerType()}")

# -------------------------------
# Bagian 4.2: Ubah symbology poligon (contoh)
# -------------------------------
from PyQt5.QtGui import QColor
if layer.geometryType() == 2:  # Polygon
    sl = layer.renderer().symbol().symbolLayers()[0]
    sl.setFillColor(QColor(70, 70, 70))
    sl.setStrokeColor(QColor(255, 255, 255))
    sl.setStrokeWidth(0.5)
    layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(layer.id())
    print("Symbology poligon berhasil diubah")

# -------------------------------
# Bagian 4.3: Ubah symbology garis (contoh)
# -------------------------------
from PyQt5.QtCore import Qt
if layer.geometryType() == 1:  # Line
    sl = layer.renderer().symbol().symbolLayers()[0]
    sl.setColor(QColor(30, 30, 30))
    sl.setWidth(0.8)
    sl.setPenStyle(Qt.DashLine)
    layer.triggerRepaint()
    print("Symbology garis diubah")

# -------------------------------
# Bagian 4.4: Ubah symbology titik (contoh)
# -------------------------------
if layer.geometryType() == 0:  # Point
    sl = layer.renderer().symbol().symbolLayers()[0]
    sl.setFillColor(QColor(40, 40, 40))
    sl.setStrokeColor(QColor(200, 200, 200))
    sl.setSize(4.0)
    sl.setShape(QgsSimpleMarkerSymbolLayer.Shape.Square)
    layer.triggerRepaint()
    print("Symbology titik diubah")
