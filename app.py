from flask import Flask, request, jsonify
import assignment  # import your functions from your script

app = Flask(__name__)

@app.route('/convert_pdf', methods=['POST'])
def convert_pdf():
    data = request.get_json()  # get data from POST request
    pdf_path = data['pdf_path']
    txt_path = data['txt_path']
    assignment.pdf_to_txt(pdf_path, txt_path)  # call your function
    return jsonify({'message': f'Converted {pdf_path} to {txt_path}'}), 200

@app.route('/extract_data', methods=['POST'])
def extract_data():
    data = request.get_json()  # get data from POST request
    cv_files = data['cv_files']
    output_file = data['output_file']
    assignment.extract_and_save_data(cv_files, output_file)  # call your function
    return jsonify({'message': f'Data saved to {output_file}'}), 200

if __name__ == '__main__':
    app.run(debug=True)
