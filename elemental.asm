// ; Definitions
arch    md.cpu
endian  msb

// ; Patched Output
output  "bin/elemental_master_br.bin",create

// ; Configuration
constant CONFIG_LANGUAGE(PORTUGUESE)

define   CONFIG_ROM_NAME("ELEMENTAL MASTER             ")
define   CONFIG_ROM_REGION("U")
define   CONFIG_ROM_SIZE(eof)


origin ROM_START
    // ; Original File
    insert "bin/Elemental Master.md"
    
    // ; Includes
    include "asm/macros.asm"
    include "asm/constants.asm"

if (CONFIG_LANGUAGE == ENGLISH) {

    //include "text/en/credits.asm"
    //include "text/en/menu.asm"
    //include "text/en/locations.asm"
    //include "text/en/dialogue.asm"
}


if (CONFIG_LANGUAGE == PORTUGUESE) {

    define   CONFIG_ROM_NAME("MESTRE ELEMENTAL V1.0 BETA")
    define   CONFIG_ROM_REGION("JUE")

    
    include "text/br/dialogos.asm"
    
   
}

include "asm/pointers.asm"

origin $00000150
    db {CONFIG_ROM_NAME}

origin $000001A4
    dl {CONFIG_ROM_SIZE}

origin $000001F0
    db {CONFIG_ROM_REGION}

    define CONFIG_ROM_SIZE(pc())

eof: