import qrcode
import numpy as np

def generate_qr_binary(url="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUIcmlja3JvbGygBwE%3D"):
    # Create QR code object with automatic version and medium error correction
    qr = qrcode.QRCode(
        version=None,  # automatic version based on data length
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=1,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    # Get the matrix of the QR code (True=black, False=white)
    matrix = qr.get_matrix()

    # Convert to numpy array of ints (1 and 0)
    binary_matrix = np.array(matrix).astype(int)

    # Print QR code resolution
    print(f"QR code resolution: {len(binary_matrix)} x {len(binary_matrix[0])}")

    # Print the binary matrix rows as strings of 0s and 1s
    for row in binary_matrix:
        print(''.join(str(bit) for bit in row))

if __name__ == "__main__":
    generate_qr_binary()
