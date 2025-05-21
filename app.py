from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

# فایل موقت برای ذخیره رشته‌ها
DATA_FILE = 'saved_strings.json'

# اطمینان از وجود فایل
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f)

@app.route('/')
def index():
    # رندر صفحه HTML
    return render_template('index.html')

@app.route('/save', methods=['GET'])
def save_string():
    # دریافت مقدار string از پارامتر GET
    input_string = request.args.get('text')
    
    if input_string:
        # خواندن داده‌های قبلی
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # افزودن رشته جدید
        data.append(input_string)
        
        # ذخیره در فایل
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        
        return f"رشته '{input_string}' با موفقیت ذخیره شد!"
    else:
        return "لطفاً یک مقدار string در پارامتر 'text' ارسال کنید!"

@app.route('/get_strings', methods=['GET'])
def get_strings():
    # ارسال داده‌های ذخیره‌شده به صورت JSON
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return json.dumps(data, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)