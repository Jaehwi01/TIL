const concat= (str1, str2) => {
    return `${str1}-${str2}`
}

const checkLongStr = (string) =>{
    if (string.length >= 10)
    {   return true}
    else{
        return false
    }
}

if (checkLongStr(concat('h', 'hacking'))){
    console.log('long string')
}else{
    console.log('short string')
}