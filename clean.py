import os
import re
import pysnooper
@pysnooper.snoop()
def clean():
    dirs = os.listdir('news_materials')
    for dir in dirs:
        arts = os.listdir(f'news_materials/{dir}')
        for art in arts:
            with open(f'news_materials/{dir}/{art}', 'r') as f:
                t = f.read()
                pattern = re.compile('Scan QR.*Account', re.DOTALL)
                new_str = pattern.sub('', t)
            with open(f'news_materials/{dir}/{art}', 'w') as f:
                f.write(new_str)    
clean()                