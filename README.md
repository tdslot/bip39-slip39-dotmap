# Mnemonic Dot Pattern Mapping

This repository provides tools and documentation for mapping BIP39 and SLIP39 mnemonic phrases to visual dot patterns. This can be useful for physical backups of your recovery phrases.
### Reversed Mapping Explanation

Yoseyomo designed their system so that binary numbers are read intuitively, from left to right, starting with the smallest values (1, 2, 4, 8, 16, ...), making it user-friendly. This "reversed" variant, available for both BIP39 and SLIP39, simplifies practical implementation, even though it varies slightly from the technical standard.

## BIP39 Dot Pattern Mapping

BIP39 is a standard for generating mnemonic recovery phrases (12-24 words) to recover private keys. It transforms private keys into easy-to-remember words.

### How BIP39 Works (Example: Word Index 628)

1.  **Find largest number ≤ 628:** 512.
2.  **Subtract:** 628 - 512 = 116.
3.  **Continue with next largest numbers:**
    *   **64:** 116 - 64 = 52.
    *   **32:** 52 - 32 = 20.
    *   **16:** 20 - 16 = 4.
    *   **4:** 4 - 4 = 0.
    *   Combination: **512 + 64 + 32 + 16 + 4 = 628**.

In the standard (non-reversed) mapping, binary numbers are read from left to right (largest to smallest value).

### Dot Pattern Representation (12 dots)

Each word is represented by 12 dots, corresponding to the values:
2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1

For instance:

*   `#63 amazing = 32, 16, 8, 4, 2, 1`
    `| ○○○○ | ○○●● | ●●●● |`
*   `#977 key = 512 + 256 + 128 + 64 + 16 + 1`
    `| ○○●● | ●●○● | ○○○● |`
*   `#996 ladder = 16 + 8 + 4 + 2 + 1`
    `| ○○●● | ●●●○ | ○●○○ |`
*   `#997 lady = 16 + 8 + 4 + 2 + 1`
    `| ○○●● | ●●●○ | ○●○● |`

This table divides the 12 points into three columns for readability.
- [Full BIP39 Dot Pattern Mapping Table](bip39-dot-pattern-mapping.md)
- [Full BIP39 Dot Pattern Mapping Table (Reversed)](bip39-dot-pattern-mapping-reversed.md)

### BIP39 Reversed Examples

Each word is represented by 12 dots, corresponding to the values:
1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048

*   `#63 amazing = 1 + 2 + 4 + 8 + 16 + 32`
    `| ●●●● | ○○●● | ○○○○ |`
*   `#977 key = 1 + 16 + 64 + 128 + 256 + 512`
    `| ○○○● | ●●○● | ○○●● |`

## SLIP39 Dot Pattern Mapping

SLIP39 is an advanced standard using Shamir's Secret Sharing to divide recovery phrases into multiple fragments (shares) for enhanced security.

### How SLIP39 Works (Example: Word Index 308)

1.  **Find largest number ≤ 308:** 256.
2.  **Subtract:** 308 - 256 = 52.
3.  **Continue with next largest numbers:**
    *   **32:** 52 - 32 = 20.
    *   **16:** 20 - 16 = 4.
    *   **4:** 4 - 4 = 0.
    *   Combination: **256 + 32 + 16 + 4 = 308**.

In the standard (non-reversed) mapping, binary numbers are read from left to right (largest to smallest value).

### Dot Pattern Representation (12 dots)

Each word is represented by 12 dots, corresponding to the values:
2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1

For instance:

*   `#1 academic = 1`
    `| ○○○○ | ○○○○ | ○○○● |`
*   `#1024 zero = 1024`
    `| ○●○○ | ○○○○ | ○○○○ |`
*   `#496 kernel = 512 + 256 + 128 + 64 + 32`
    `| ○○○● | ●●●● | ○○○○ |`
*   `#497 keyboard = 512 + 256 + 128 + 64 + 32 + 1`
    `| ○○○● | ●●●● | ○○○● |`

This table divides the 12 points into three columns for readability.
- [Full SLIP39 Dot Pattern Mapping Table](slip39-dot-pattern-mapping.md)
- [Full SLIP39 Dot Pattern Mapping Table (Reversed)](slip39-dot-pattern-mapping-reversed.md)

### SLIP39 Reversed Examples

Each word is represented by 12 dots, corresponding to the values:
1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048

*   `#1 academic = 1`
    `| ●○○○ | ○○○○ | ○○○○ |`
*   `#3 acne = 1 + 2`
    `| ●●○○ | ○○○○ | ○○○○ |`
*   `#374 friendly = 2 + 4 + 16 + 32 + 64 + 256`
    `| ○●●○ | ●●●○ | ●○○○ |`
*   `#628 orange = 4 + 16 + 32 + 64 + 512`
    `| ○○●○ | ●●●○ | ○●○○ |`
*   `#1024 zero = 1024`
    `| ○○○○ | ○○○○ | ○○●○ |`

---
*Based on documentation from 
- [Yoseyomo SLIP39 Word List](https://www.yoseyomo.com/en/pages/slip39-word-list), 
- [Yoseyomo BIP39 Word List](https://www.yoseyomo.com/en/pages/bip39-word-list) and 
- [OneKeyHQ/bip39-dotmap](https://github.com/OneKeyHQ/bip39-dotmap).*