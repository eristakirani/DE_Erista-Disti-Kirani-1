DELIMITER // 
CREATE PROCEDURE cobaIF( 
    IN bil INT(3) 
) 
BEGIN 
    /*Deklarasi Variabel*/ 
    DECLARE str VARCHAR(50); 
    if (bil<0) then 
        SET str ='Bilangan Positif'; 
    ELSE 
        SET str='Bilangan Negatif'; 
    END if; 
    SELECT str; 
END// 
DELIMITER;