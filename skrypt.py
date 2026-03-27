import hashlib
import os
import binascii

# 1. Zdefiniowanie hasła użytkownika
password = "MojeUltraTajneHaslo123!" 

# 2. Generowanie unikalnego 'solenia' (salt) dla zwiększenia bezpieczeństwa
# Sól to losowy ciąg danych dodawany do hasła, aby uniknąć ataku 'tęczowych tablic'.
salt = os.urandom(32) 
# os.urandom(32) generuje 32 losowe bajty

# 3. Haszowanie hasła przy użyciu bezpiecznej metody PBKDF2
# PBKDF2 jest zalecaną metodą, ponieważ jest celowo 'powolna', 
# co utrudnia atakującym testowanie milionów haseł na sekundę.

key = hashlib.pbkdf2_hmac(
    'sha256',          # Algorytm haszujący
    password.encode('utf-8'), # Hasło musi być zakodowane do bajtów
    salt,              # Sól (losowość)
    100000             # Liczba iteracji (im więcej, tym bezpieczniej)
)

# 4. Łączenie soli i haszowanego klucza (do zapisania w bazie danych)
# Musimy zapisać sól wraz z hasłem, aby móc je zweryfikować później!
storage_hash = salt + key
final_hash_to_store = binascii.hexlify(storage_hash).decode('ascii')

print(f"--- Przykład Haszowania Hasła ---")
print(f"Hasło Oryginalne: {password}")
print(f"Wygenerowana Sól (32 bajty): {binascii.hexlify(salt)}")
print(f"Finalny Hash (do bazy danych):\n{final_hash_to_store}")
print(f"\nUWAGA: Hasz ma długość 96 bajtów (64 bajty klucza + 32 bajty soli)")

# Funkcja do weryfikacji hasła
def verify_password(stored_hash, provided_password):
    # 1. Dekodowanie hasza zapisanego w bazie
    stored_hash_bytes = binascii.unhexlify(stored_hash)
    
    # 2. Wydobycie soli (pierwsze 32 bajty) i klucza (reszta)
    salt_from_storage = stored_hash_bytes[:32]
    key_from_storage = stored_hash_bytes[32:]

    # 3. Ponowne haszowanie hasła podanego przez użytkownika, używając ZAPISANEJ soli
    new_key = hashlib.pbkdf2_hmac(
        'sha256', 
        provided_password.encode('utf-8'), 
        salt_from_storage, 
        100000
    )

    # 4. Porównanie kluczy
    return new_key == key_from_storage

# Test Weryfikacji:
print("\n--- Test Weryfikacji ---")
# Przypadek A: Poprawne hasło
correct_pass = "MojeUltraTajneHaslo123!"
is_correct = verify_password(final_hash_to_store, correct_pass)
print(f"Hasło '{correct_pass}' jest poprawne? {'TAK' if is_correct else 'NIE'}")

# Przypadek B: Niepoprawne hasło
wrong_pass = "ZleHaslo!"
is_wrong = verify_password(final_hash_to_store, wrong_pass)
print(f"Hasło '{wrong_pass}' jest poprawne? {'TAK' if is_wrong else 'NIE'}")