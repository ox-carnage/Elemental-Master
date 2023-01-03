// Control Macros
macro text(TEXT) {
    table "tbl/text.tbl"
    db {TEXT}
}
macro menu_text(TEXT) {
    table "tbl/text.tbl"
    db {TEXT}
    end()
}
macro text_location(TEXT) {
    table "tbl/text.tbl"
    db {TEXT}
    end()
}
macro credits(TEXT) {
    table "tbl/text.tbl"
    db {TEXT}
}
macro dialogue_text(TEXT) {
    table "tbl/text.tbl"
    db {TEXT}
    break_line()
}


macro break_line() { 
    dw $0d0a
}
macro end() {
    db $00
}
macro start_line() {
   dl STARTLINE
}

macro text_align() {
    dl ALIGNTEXT
}
macro  character_spider() { 
    dw CHARACTERSPIDER
}
macro  index() {    
    dw INDEX
}
macro character_other() {
    dw CHARACTEROTHER
}
macro pula_linha1() {
    dw LINHA1
}
macro pula_linha2() {
    dw LINHA2
}
macro indexcredit() {
    dl $0002
}
macro fim() {
    dl $00060300
}