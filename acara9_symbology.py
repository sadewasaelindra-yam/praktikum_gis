# ============================================
# Nama Lengkap : Sadewa Saelindra
# NIM          : 25/568929/SV/27564
# Tanggal      : 7 Mei 2026
# File         : acara9_symbology.py
# Deskripsi    : Script mandiri untuk ubah symbology layer poligon
# ============================================

from PyQt5.QtGui import QColor
from qgis.core import QgsProject

# --- KONFIGURASI (WAJIB DIUBAH) ---
NAMA_LAYER = "Batas_kecamatan_kab.bandung"   # pilih layer poligonmu
WARNA_ISI  = (200, 200, 255)                 # isi poligon (biru muda)
WARNA_TEPI = (0, 0, 0)                       # garis tepi (hitam)
TEBAL_TEPI = 0.8                             # ketebalan garis (mm)
OPACITY    = 0.85                            # transparansi (0.5 - 1.0)

# --- FUNGSI (tidak perlu diubah) ---
def ubah_symbology(nama_layer, warna_isi, warna_tepi, tebal_tepi, opacity):
    """Mengubah symbology layer poligon dan mencetak laporan perubahan."""
    layers = QgsProject.instance().mapLayersByName(nama_layer)
    if not layers:
        print(f"ERROR: Layer '{nama_layer}' tidak ditemukan.")
        print("Periksa NAMA_LAYER di bagian konfigurasi.")
        return False

    layer = layers[0]
    print(f"Layer    : {layer.name()}")
    print(f"Geometri : {layer.geometryType()}")

    if layer.geometryType() != 2:
        print("PERINGATAN: Script ini dirancang untuk layer poligon (tipe 2).")

    sl = layer.renderer().symbol().symbolLayers()[0]

    # Simpan nilai lama untuk laporan
    isi_lama = sl.fillColor().name()
    tepi_lama = sl.strokeColor().name()

    # Terapkan perubahan
    sl.setFillColor(QColor(*warna_isi))
    sl.setStrokeColor(QColor(*warna_tepi))
    sl.setStrokeWidth(tebal_tepi)
    layer.setOpacity(opacity)
    layer.triggerRepaint()
    iface.mapCanvas().refresh()

    print("\n- Perubahan yang diterapkan")
    print(f" Warna isi  : {isi_lama} -> QColor{warna_isi}")
    print(f" Warna tepi : {tepi_lama} -> QColor{warna_tepi}")
    print(f" Tebal tepi : {tebal_tepi} mm")
    print(f" Opacity    : {opacity}")
    print("Symbology berhasil diperbarui.")
    return True

# --- JALANKAN ---
ubah_symbology(
    nama_layer=NAMA_LAYER,
    warna_isi=WARNA_ISI,
    warna_tepi=WARNA_TEPI,
    tebal_tepi=TEBAL_TEPI,
    opacity=OPACITY
)
