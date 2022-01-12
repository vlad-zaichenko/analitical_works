SELECT * FROM 'adverts'
LEFT OUTER JOIN 'coasts' on adverts.advert_id = coasts.advert_id 
WHERE coast < 500
