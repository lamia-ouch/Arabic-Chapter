import tokenizer
from tokenizer import tokenization

text = """قراءة د. أحمد خالد توفيق في رواية «جمهورية كأن» للروائي علاء الأسواني، المشروع الذي ظل يتحدث ولم يفارق ذهنه 
لحظة.قرأت القصة .. الحقيقة التي لا يماري فيها أحد هي أن الرجل ممتع حقًا. وهو مصر على أن يظل ممتعًا مهما كره النقاد 
ذلك. هو يؤمن بفن الرواية بتعريفه العتيق؛ أي (الحكي). أن تنتظر حتى الليل في لهفة لتعرف ما حدث . وهو مصر على الطريقة 
الديكنزية في أن يجعل الرواية متحفًا للشخصيات الفريدة الممتعة. بحيث أنك قد تنسى الرواية لكن الشخصيات تلاحقك طيلة 
الوقت.  هناك مكونات وأجزاء معينة يستعملها علاء الأسواني مثل الميكانو من قصة لأخرى، فيعيد ترتيبها ليخلق مواقف جديدة. 
مثلًا شخصية الضابط المتدين الذي يعذب الأبرياء ولا يفوت فرضًا – الثري الراقي الذي يعد بالمفهوم التقليدي فاسد الأخلاق، 
لكنه أكثر شخصيات القصة طهرًا وصدقًا، وبالطبع هناك الحب الجسدي بينه وبين خادمة أو مدبرة منزل نبيلة تحبه فعلًا، وهناك 
ضغوط المجتمع ضده بين أخت مثل دولت أو زوجة أو أولاد.. هناك علاقات تدور في قمة المجتمع فوق رءوسنا ولا نعرف عنها أي شيء . 
لم يستعمل الأسواني قطعة ميكانو الشاب الشاذ جنسيًا هذه المرة، وإن استخدم قطعة ميكانو مهمة جدًا هي ضحية الأمن الذي آمن 
بالعدالة ثم أدرك مع الوقت أن ديانة الدولة هي الظلم، وأن الدم هو الحل الوحيد. لن أعطي تفاصيل حتى لا أدمر نهاية 
الرواية، لكنها نهاية قوية جدًا."""

tokenizer=tokenization(text)

print('Sentences :')
for sent in tokenizer.sentences :
  print('['+sent+']')
print()
print('Tokens :')
for token in tokenizer.tokens :
  print(token)