$x = 4
for($i=1; $i -le $x; $i++){ 
   #changed -le $x to -le $x - $i
   for($k=1; $k -le $x -$i; $k++ ){
      Write-Host -NoNewLine " "
   }

   for($j=1; $j -le 2 * $i - 1; $j++){ 
     Write-Host -NoNewLine "D" 
   }

   Write-Host " "
}
