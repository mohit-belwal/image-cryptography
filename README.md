Secret message can be encoded in a PNG image.
Used PIL module for all Image functions.

Encryption:-
  Message is first encrypted by RSA algorithm using public key.
  Encrypted message is embedded in a PNG image by LSB embedding method.
  Encoded image is saved as a new PNG image.
  
Decryption:-
  Encrypted message is decoded from encoded image.
  Original message is retrieved by decryption of encrypted message through RSA algorithm using private key.

RSA algorithm is a safe mode of encrypting data. It comes under Asymmetric Cryptography as it works on two different keys.
