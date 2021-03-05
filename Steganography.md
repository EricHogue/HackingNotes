# Steganography

* Get strings in file
    `strings FILE | awk 'length($0)>10' | sort -u | less`
* Check for hidden files
    `binwalk FILE`
* Check for corruption in png file
    `pngcheck -v FILE`
* Extract file metadata
    `exiftool FILE`
* Stegoveritas
    `stegoveritas FILE`
* Check for hidden file
    `stegoveritas -steghide`
* Extract file
    `steghide extract -sf cute-alien.jpg`
* Bruteforce steghide
    `stegcracker`
