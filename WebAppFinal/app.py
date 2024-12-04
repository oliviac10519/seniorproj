# import pandas as pd
# from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
# import os
# import matplotlib.pyplot as plt
# from werkzeug.utils import secure_filename
# import matplotlib
# matplotlib.use('Agg') 

# from flask import send_file



# app= Flask(__name__)
# app.config['UPLOAD_FOLDER']='uploads/'
# app.config['CHARTS_FOLDER']='static/charts/'
# app.secret_key='klqnmzo'


# os.makedirs(app.config['UPLOAD_FOLDER'],exist_ok=True)
# os.makedirs(app.config['CHARTS_FOLDER'],exist_ok=True)

# def create_pc1(df, index, val, name, title):
#     if df.empty:
#         return None, None
#     pivot=pd.pivot_table(df, index=index, values=val, aggfunc='sum' if val == "Recurring ACV (USD)" else 'count')
#     pivot.plot(kind='bar', title=title)
#     chart_path = os.path.join(app.config['CHARTS_FOLDER'], name)
#     plt.savefig(chart_path)
#     plt.close()
#     return pivot.to_html(classes='table table-striped'), name
# # def create_pc2(data, index, stage, name, title):
# #     if data.empty:
# #         return None, None

# #     chart_path = os.path.join(app.config['CHARTS_FOLDER'], name)
# #     os.makedirs(os.path.dirname(chart_path), exist_ok=True)

# #     # Plotting code...
# #     # (same as before)

# #     plt.savefig(chart_path)
# #     plt.close()

# #     pivot_html = data.to_html(classes='table table-striped', index=True)
# #     return pivot_html, name

# def create_pc2(data, index, stage, name, title):

#     if data.empty:
#         return None, None


#     chart_path = os.path.join(app.config['CHARTS_FOLDER'], name)
#     #****os.makedirs(os.path.dirname(chart_path), exist_ok=True)

#     ax = data.plot(kind="bar", width=0.8, figsize=(10, 6), color=["#1f77b4", "#ff7f0e"])
#     ax.set_title(title, fontsize=14)
#     ax.set_xlabel(index, fontsize=12)
#     ax.set_ylabel("Recurring ACV (USD)", fontsize=12)
#     ax.legend(["Timeframe 1", "Timeframe 2"], loc="best")
#     plt.xticks(rotation=45, ha="right")

#     plt.tight_layout()
#     plt.savefig(chart_path)
#     plt.close()

#     pivot_html = data.to_html(classes='table table-striped', index=True)
#     return pivot_html, name

   
# def process_data(data1, data2, group_by, chart_name, chart_title):
#     merged_df = pd.merge(data1, data2, how='outer', on=[group_by])
#     if merged_df.empty:
#         return None, None
#     aggregated = merged_df.groupby(group_by)[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#     aggregated.columns = ['Timeframe 1', 'Timeframe 2']
#     return create_pc1(aggregated, group_by, "Selling Stage", chart_name, chart_title)





# def just_one(dftf1,win,lose):
#    closed_won1=dftf1.loc[(dftf1['Selling Stage'] == win)]
#    closed_lost1=dftf1.loc[(dftf1['Selling Stage'] == lose)]
#    sum_won1=closed_won1['Recurring ACV (USD)'].sum()
#    #pivot_won1=pd.pivot_table(closed_won1, index=["Selling Team"], values=["Selling Stage"], aggfunc='count')
#    #pivot_lost1=pd.pivot_table(closed_lost1, index=["Selling Team"], values=["Selling Stage"], aggfunc='count')
  
#    charts=[]
#    pivots_won=[]

#    pivot_html, chart_file=create_pc1(closed_won1, "Selling Team", "Selling Stage", "closed_won_team1.png", "Closed Won by Selling Team (Count)")

#    if pivot_html and chart_file:
#        pivots_won.append(pivot_html)
#        charts.append(chart_file)
#         # cleaned_html = pivot_html.strip()
#         # pivots_won.append(cleaned_html)
#         # charts.append(chart_file)
#    pivot_html, chart_file = create_pc1(closed_won1, "Selling Team", "Recurring ACV (USD)", "closed_won_team_usd.png", "Closed Won by Selling Team (USD)")
#    if pivot_html and chart_file:
#         pivots_won.append(pivot_html)
#         charts.append(chart_file)

        
#    pivot_html, chart_file = create_pc1(closed_won1, "Seller Name", "Selling Stage", "closed_won_seller_1.png", "Closed Won by Seller (Count)")
#    if pivot_html and chart_file:
#         pivots_won.append(pivot_html)
#         charts.append(chart_file)  
#    pivot_html, chart_file = create_pc1(closed_won1, "Seller Name", "Recurring ACV (USD)", "closed_won_seller_usd.png", "Closed Won by Seller (USD)")
#    if pivot_html and chart_file:
#         pivots_won.append(pivot_html)
#         charts.append(chart_file) 
#    return pivots_won, charts, sum_won1


# def compare_two(dftf1, dftf2, win, lose):
#     closed_won1 = dftf1.loc[dftf1['Selling Stage'] == win]
#     closed_won2 = dftf2.loc[dftf2['Selling Stage'] == win]

#     charts = []
#     pivots_won = []

#     merged_won = pd.merge(closed_won1, closed_won2, how='outer', on=['Selling Team'])
#     if not merged_won.empty:
#         aggregated = merged_won.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated.columns = ['Timeframe 1', 'Timeframe 2']
#         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
#                                             "closed_won_team11.png", 
#                                             "Closed Won by Selling Team (in USD)")
#         if chart_file:
#             charts.append(chart_file)
#         if pivot_html:
#             pivots_won.append(pivot_html)

#     merged_won_seller = pd.merge(closed_won1, closed_won2, how='outer', on=['Seller Name'])
#     if not merged_won_seller.empty:
#         aggregated_seller = merged_won_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
#         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None,  "closed_won_seller11.png",  "Closed Won by Seller (in USD)")
#         if chart_file:
#             charts.append(chart_file)
#         if pivot_html:
#             pivots_won.append(pivot_html)


#     closed_lost1 = dftf1.loc[dftf1['Selling Stage'] == lose]
#     closed_lost2 = dftf2.loc[dftf2['Selling Stage'] == lose]

#     merged_lost = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Selling Team'])
#     if not merged_lost.empty:
#         aggregated = merged_lost.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated.columns = ['Timeframe 1', 'Timeframe 2']
#         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, "closed_lost_team11.png",  "Closed Lost by Selling Team (in USD)")
#         if chart_file:
#             charts.append(chart_file)
#         if pivot_html:
#             pivots_won.append(pivot_html)

#     merged_lost_seller = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Seller Name'])
#     if not merged_lost_seller.empty:
#         aggregated_seller = merged_lost_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
#         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None,  "closed_lost_seller11.png",  "Closed Lost by Seller (in USD)")
#         if chart_file:
#             charts.append(chart_file)
#         if pivot_html:
#             pivots_won.append(pivot_html)

#     sum_won1 = closed_won1['Recurring ACV (USD)'].sum() + closed_won2['Recurring ACV (USD)'].sum()
#     return pivots_won, charts, sum_won1


# # def compare_two(dftf1, dftf2, win, lose):
# #     closed_won1 = dftf1.loc[dftf1['Selling Stage'] == win]
# #     closed_won2 = dftf2.loc[dftf2['Selling Stage'] == win]

# #     charts = []
# #     pivots_won = []

# #     merged_won = pd.merge(closed_won1, closed_won2, how='outer', on=['Selling Team'])
# #     if not merged_won.empty:
# #         aggregated = merged_won.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
# #         aggregated.columns = ['Timeframe 1', 'Timeframe 2']
# #         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
# #                                             "closed_won_team11.png", 
# #                                             "Closed Won by Selling Team (in USD)")
# #         if chart_file:
# #             charts.append(chart_file)
# #         if pivot_html:
# #             pivots_won.append(pivot_html)

# #     merged_won_seller = pd.merge(closed_won1, closed_won2, how='outer', on=['Seller Name'])
# #     if not merged_won_seller.empty:
# #         aggregated_seller = merged_won_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
# #         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
# #         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None, 
# #                                             "closed_won_seller11.png", 
# #                                             "Closed Won by Seller (in USD)")
# #         if chart_file:
# #             charts.append(chart_file)
# #         if pivot_html:
# #             pivots_won.append(pivot_html)

# #     closed_lost1 = dftf1.loc[dftf1['Selling Stage'] == lose]
# #     closed_lost2 = dftf2.loc[dftf2['Selling Stage'] == lose]

# #     merged_lost = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Selling Team'])
# #     if not merged_lost.empty:
# #         aggregated = merged_lost.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
# #         aggregated.columns = ['Timeframe 1', 'Timeframe 2']
# #         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
# #                                             "closed_lost_team11.png", 
# #                                             "Closed Lost by Selling Team (in USD)")
# #         if chart_file:
# #             charts.append(chart_file)
# #         if pivot_html:
# #             pivots_won.append(pivot_html)

# #     merged_lost_seller = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Seller Name'])
# #     if not merged_lost_seller.empty:
# #         aggregated_seller = merged_lost_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
# #         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
# #         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None, 
# #                                             "closed_lost_seller11.png", 
# #                                             "Closed Lost by Seller (in USD)")
# #         if chart_file:
# #             charts.append(chart_file)
# #         if pivot_html:
# #             pivots_won.append(pivot_html)

# #     sum_won1 = closed_won1['Recurring ACV (USD)'].sum() + closed_won2['Recurring ACV (USD)'].sum()
# #     return pivots_won, charts, sum_won1



# # def compare_two(dftf1,dftf2,win,lose):
# #     closed_won1 = dftf1.loc[dftf1['Selling Stage'] == win]
# #     closed_won2 = dftf2.loc[dftf2['Selling Stage'] == win]

# #     merged_won = pd.merge(closed_won1, closed_won2, how='outer', on=['Selling Team'])
# #     if not merged_won.empty:
# #         aggregated = merged_won.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
# #         aggregated.columns = ['Timeframe 1', 'Timeframe 2']  
        
# #         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
# #                                             "closed_won_team11.png", 
# #                                             "Closed Won by Selling Team (in USD)")
# #         charts = [chart_file] if chart_file else []
# #         pivots_won = [pivot_html] if pivot_html else []
# #     else:
# #         charts = []
# #         pivots_won = []

# #     merged_won_seller = pd.merge(closed_won1, closed_won2, how='outer', on=['Seller Name'])
# #     if not merged_won_seller.empty:
# #         aggregated_seller = merged_won_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
# #         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
        
# #         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None, 
# #                                             "closed_won_seller11.png", 
# #                                             "Closed Won by Seller (in USD)")
# #         if pivot_html and chart_file:
# #             pivots_won.append(pivot_html)
# #             charts.append(chart_file)


# #     closed_lost1 = dftf1.loc[dftf1['Selling Stage'] == lose]
# #     closed_lost2 = dftf2.loc[dftf2['Selling Stage'] == lose]

# #     merged_lost = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Selling Team'])
# #     if not merged_lost.empty:
# #         aggregated = merged_lost.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
# #         aggregated.columns = ['Timeframe 1', 'Timeframe 2']  
        
# #         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
# #                                             "closed_lost_team11.png", 
# #                                             "Closed Lost by Selling Team (in USD)")
# #         charts = [chart_file] if chart_file else []
# #         pivots_won = [pivot_html] if pivot_html else []
# #     else:
# #         charts = []
# #         pivots_won = []

# #     merged_lost_seller = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Seller Name'])
# #     if not merged_lost_seller.empty:
# #         aggregated_seller = merged_lost_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
# #         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
        
# #         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None, "closed_lost_seller11.png", "Closed Lost by Seller (in USD)")
# #         if pivot_html and chart_file:
# #             pivots_won.append(pivot_html)
# #             charts.append(chart_file)
# #     sum_won1= closed_won1['Recurring ACV (USD)'].sum() + closed_won2['Recurring ACV (USD)'].sum()

 
# #     return pivots_won, charts, sum_won1










# @app.route ("/")
# def home():
#    return render_template('home.html')


# @app.route("/help", methods=["GET","POST"])
# def help():
#    return render_template('help.html')


# @app.route("/index", methods=["GET","POST"])
# def index():
#    return render_template('index.html')

# @app.route("/noresults", methods=["GET","POST"])
# def noresults():
#    return render_template('noresults.html')


# @app.route("/upload", methods=["POST"])
# def upload_file():
#    if 'file' not in request.files:
#        flash('No file uploaded')
#        return redirect(request.url)
  
  
#    file=request.files['file']


#    if file.filename=='':
#        flash('No selected file')
#        return redirect(request.url)
  
#    filename=secure_filename(file.filename)
#    file_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
#    file.save(file_path)


#    return redirect(url_for('choose', filename=filename))
# @app.route("/choose/<filename>", methods=["GET","POST"]) 
# def choose(filename):
#    if request.method=="POST":
#        if request.form.get("option")=="One Timeframe":
#            return redirect(url_for('one_route', filename=filename))
#        elif request.form.get("option")=="Two Timeframes":
#            return redirect(url_for('enter_analysis_params', filename=filename))
      
#    return render_template('choose.html', filename=filename)
#    #return redirect(url_for('enter_analysis_params', filename=filename))
#    #return redirect(url_for('enter_analysis_params'))
# #@app.route('/enter_params/<filename>', methods=['POST', 'GET']) 


# @app.route("/one_route/<filename>")
# def one_route(filename):
#    return render_template('analyze1.html', filename=filename)


# @app.route("/enter_params/<filename>")
# def enter_analysis_params(filename):
#    return render_template('analyze.html', filename=filename) 


# @app.route('/analyze1/<filename>', methods=['POST'])
# def analyze1(filename):
#    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  
#    if not os.path.exists(file_path):
#        flash('File not found. Please upload the file again.')
#        return redirect(url_for('noresults'))


#    try:
#        dataFrameOriginal = pd.read_excel(file_path)
#        oppID = request.form.get('oppID')
#        dataFrameOriginal.drop_duplicates(subset=[oppID], keep='first',  inplace=True)
#        dataFrameOriginal['Created Date'] = pd.to_datetime(dataFrameOriginal['Created Date'], errors='coerce')
#        dataFrameOriginal['Date Closed'] = pd.to_datetime(dataFrameOriginal['Date Closed'], errors='coerce')
      
#        timeframe1_1 = request.form.get('timeframe1_1')
#        timeframe1_2 = request.form.get('timeframe1_2')
      
      
#        if timeframe1_1 and timeframe1_2 :
#            dftf1 = dataFrameOriginal.loc[
#                (dataFrameOriginal['Created Date'] >= timeframe1_1) &
#                (dataFrameOriginal['Created Date'] <= timeframe1_2)]
#         #    filename='Clean_Sorted.xlsx'
#         #    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         #    dftf1.to_excel(filepath, index=False)
#        else:
#            flash ('Timeframe inputs required')
#            return redirect(url_for('one_route', filename=filename))
          
#        win_stage = request.form.get('win_stage', type=int)
#        lose_stage = request.form.get('lose_stage', type=int)
      
#        pivots_won, charts, sum_won1 = just_one(dftf1, win_stage, lose_stage)
#        return render_template('results.html', results=pivots_won, charts=charts, sum_won1=sum_won1)
  
#    except Exception as e:
#        flash(f"Error during analysis: {e}")
#        return redirect(url_for('noresults'))




# @app.route('/analyze/<filename>', methods=['POST'])
# def analyze(filename):
#    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  
#    if not os.path.exists(file_path):
#        flash('File not found. Please upload the file again.')
#        return redirect(url_for('noresults'))


#    try:
   
#        dataFrameOriginal = pd.read_excel(file_path)
#        oppID = request.form.get('oppID')
#        dataFrameOriginal.drop_duplicates(subset=[oppID], keep='first',  inplace=True)
#        dataFrameOriginal['Created Date'] = pd.to_datetime(dataFrameOriginal['Created Date'], errors='coerce')
#        dataFrameOriginal['Date Closed'] = pd.to_datetime(dataFrameOriginal['Date Closed'], errors='coerce')
      
  
#        timeframe1_1 = request.form.get('timeframe1_1')
#        timeframe1_2 = request.form.get('timeframe1_2')
#        timeframe2_1 = request.form.get('timeframe2_1')
#        timeframe2_2 = request.form.get('timeframe2_2')
  
#        if timeframe1_1 and timeframe1_2 and timeframe2_1 and timeframe2_2:
#            dftf1 = dataFrameOriginal.loc[
#                (dataFrameOriginal['Created Date'] >= timeframe1_1) &
#                (dataFrameOriginal['Created Date'] <= timeframe1_2)]
#            dftf2 = dataFrameOriginal.loc[
#                (dataFrameOriginal['Created Date'] >= timeframe2_1) &
#                (dataFrameOriginal['Created Date'] <= timeframe2_2)]
#            merged_df = pd.merge(dftf1, dftf2, on='Created Date')
#            filename='Clean_Sorted.xlsx'
#            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#            merged_df.to_excel(filepath, index=False)
          
#        win_stage = request.form.get('win_stage', type=int)
#        lose_stage = request.form.get('lose_stage', type=int)

#        pivots_won, charts, sum_won1 = compare_two(dftf1, dftf2, win_stage, lose_stage)
#        return render_template('results.html', results=pivots_won, charts=charts, sum_won1=sum_won1)

#    except Exception as e:
#        flash(f"Error during analysis: {e}")
#        return redirect(url_for('noresults'))
  
# @app.route('/static/charts/<filename>')
# def serve_chart(filename):
#    return send_from_directory(app.config['CHARTS_FOLDER'],filename)
# @app.route('/pivot', methods=['GET','POST'])
# def resultsp():
#     return render_template('resultsp.html')

# # @app.route('/download')
# # def downloadExcel():
# #     root_path = "path_to_your_file"
# #     filename = "your_file_name.xlsx"
# #     file_path = os.path.join(root_path, filename)
# #     return send_file(file_path)

# @app.route('/download/<filename>')
# def download_excel(filename):
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     if os.path.exists(file_path):
#         return send_file(file_path, as_attachment=True)
#     else:
#         flash("File not found.")
#         return redirect(url_for('noresults'))


# if __name__=="__main__":
#    app.run(debug=True, port= 5001)



import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
import matplotlib
matplotlib.use('Agg') 

#from flask import send_file



app= Flask(__name__)
app.config['UPLOAD_FOLDER']='uploads/'
app.config['CHARTS_FOLDER']='static/charts/'
app.secret_key='klqnmzo'


os.makedirs(app.config['UPLOAD_FOLDER'],exist_ok=True)
os.makedirs(app.config['CHARTS_FOLDER'],exist_ok=True)

def create_pc1(df, index, val, name, title):
    if df.empty:
        return None, None
    pivot=pd.pivot_table(df, index=index, values=val, aggfunc='sum' if val == "Recurring ACV (USD)" else 'count')
    pivot.plot(kind='bar', title=title)
    chart_path = os.path.join(app.config['CHARTS_FOLDER'], name)
    plt.savefig(chart_path)
    plt.close()
    return pivot.to_html(classes='table table-striped'), name
# def create_pc2(data, index, stage, name, title):
#     if data.empty:
#         return None, None

#     chart_path = os.path.join(app.config['CHARTS_FOLDER'], name)
#     os.makedirs(os.path.dirname(chart_path), exist_ok=True)

#     # Plotting code...
#     # (same as before)

#     plt.savefig(chart_path)
#     plt.close()

#     pivot_html = data.to_html(classes='table table-striped', index=True)
#     return pivot_html, name

def create_pc2(data, index, stage, name, title):

    if data.empty:
        return None, None


    chart_path = os.path.join(app.config['CHARTS_FOLDER'], name)
    #****os.makedirs(os.path.dirname(chart_path), exist_ok=True)

    ax = data.plot(kind="bar", width=0.8, figsize=(10, 6), color=["#1f77b4", "#ff7f0e"])
    ax.set_title(title, fontsize=14)
    ax.set_xlabel(index, fontsize=12)
    ax.set_ylabel("Recurring ACV (USD)", fontsize=12)
    ax.legend(["Timeframe 1", "Timeframe 2"], loc="best")
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    pivot_html = data.to_html(classes='table table-striped', index=True)
    return pivot_html, name

   
def process_data(data1, data2, group_by, chart_name, chart_title):
    merged_df = pd.merge(data1, data2, how='outer', on=[group_by])
    if merged_df.empty:
        return None, None
    aggregated = merged_df.groupby(group_by)[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
    aggregated.columns = ['Timeframe 1', 'Timeframe 2']
    return create_pc1(aggregated, group_by, "Selling Stage", chart_name, chart_title)





def just_one(dftf1,win,lose):
   closed_won1=dftf1.loc[(dftf1['Selling Stage'] == win)]
   closed_lost1=dftf1.loc[(dftf1['Selling Stage'] == lose)]
   sum_won1=closed_won1['Recurring ACV (USD)'].sum()
   #pivot_won1=pd.pivot_table(closed_won1, index=["Selling Team"], values=["Selling Stage"], aggfunc='count')
   #pivot_lost1=pd.pivot_table(closed_lost1, index=["Selling Team"], values=["Selling Stage"], aggfunc='count')
  
   charts=[]
   pivots_won=[]

   pivot_html, chart_file=create_pc1(closed_won1, "Selling Team", "Selling Stage", "closed_won_team1.png", "Closed Won by Selling Team (Count)")

   if pivot_html and chart_file:
       pivots_won.append(pivot_html)
       charts.append(chart_file)
        # cleaned_html = pivot_html.strip()
        # pivots_won.append(cleaned_html)
        # charts.append(chart_file)
   pivot_html, chart_file = create_pc1(closed_won1, "Selling Team", "Recurring ACV (USD)", "closed_won_team_usd.png", "Closed Won by Selling Team (USD)")
   if pivot_html and chart_file:
        pivots_won.append(pivot_html)
        charts.append(chart_file)

        
   pivot_html, chart_file = create_pc1(closed_won1, "Seller Name", "Selling Stage", "closed_won_seller_1.png", "Closed Won by Seller (Count)")
   if pivot_html and chart_file:
        pivots_won.append(pivot_html)
        charts.append(chart_file)  
   pivot_html, chart_file = create_pc1(closed_won1, "Seller Name", "Recurring ACV (USD)", "closed_won_seller_usd.png", "Closed Won by Seller (USD)")
   if pivot_html and chart_file:
        pivots_won.append(pivot_html)
        charts.append(chart_file) 
   return pivots_won, charts, sum_won1


def compare_two(dftf1, dftf2, win, lose):
    closed_won1 = dftf1.loc[dftf1['Selling Stage'] == win]
    closed_won2 = dftf2.loc[dftf2['Selling Stage'] == win]

    charts = []
    pivots_won = []

    merged_won = pd.merge(closed_won1, closed_won2, how='outer', on=['Selling Team'])
    if not merged_won.empty:
        aggregated = merged_won.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
        aggregated.columns = ['Timeframe 1', 'Timeframe 2']
        pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
                                            "closed_won_team11.png", 
                                            "Closed Won by Selling Team (in USD)")
        if chart_file:
            charts.append(chart_file)
        if pivot_html:
            pivots_won.append(pivot_html)

    merged_won_seller = pd.merge(closed_won1, closed_won2, how='outer', on=['Seller Name'])
    if not merged_won_seller.empty:
        aggregated_seller = merged_won_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
        aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
        pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None,  "closed_won_seller11.png",  "Closed Won by Seller (in USD)")
        if chart_file:
            charts.append(chart_file)
        if pivot_html:
            pivots_won.append(pivot_html)


    closed_lost1 = dftf1.loc[dftf1['Selling Stage'] == lose]
    closed_lost2 = dftf2.loc[dftf2['Selling Stage'] == lose]

    merged_lost = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Selling Team'])
    if not merged_lost.empty:
        aggregated = merged_lost.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
        aggregated.columns = ['Timeframe 1', 'Timeframe 2']
        pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, "closed_lost_team11.png",  "Closed Lost by Selling Team (in USD)")
        if chart_file:
            charts.append(chart_file)
        if pivot_html:
            pivots_won.append(pivot_html)

    merged_lost_seller = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Seller Name'])
    if not merged_lost_seller.empty:
        aggregated_seller = merged_lost_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
        aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
        pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None,  "closed_lost_seller11.png",  "Closed Lost by Seller (in USD)")
        if chart_file:
            charts.append(chart_file)
        if pivot_html:
            pivots_won.append(pivot_html)

    sum_won1 = closed_won1['Recurring ACV (USD)'].sum() + closed_won2['Recurring ACV (USD)'].sum()
    return pivots_won, charts, sum_won1


# def compare_two(dftf1, dftf2, win, lose):
#     closed_won1 = dftf1.loc[dftf1['Selling Stage'] == win]
#     closed_won2 = dftf2.loc[dftf2['Selling Stage'] == win]

#     charts = []
#     pivots_won = []

#     merged_won = pd.merge(closed_won1, closed_won2, how='outer', on=['Selling Team'])
#     if not merged_won.empty:
#         aggregated = merged_won.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated.columns = ['Timeframe 1', 'Timeframe 2']
#         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
#                                             "closed_won_team11.png", 
#                                             "Closed Won by Selling Team (in USD)")
#         if chart_file:
#             charts.append(chart_file)
#         if pivot_html:
#             pivots_won.append(pivot_html)

#     merged_won_seller = pd.merge(closed_won1, closed_won2, how='outer', on=['Seller Name'])
#     if not merged_won_seller.empty:
#         aggregated_seller = merged_won_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
#         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None, 
#                                             "closed_won_seller11.png", 
#                                             "Closed Won by Seller (in USD)")
#         if chart_file:
#             charts.append(chart_file)
#         if pivot_html:
#             pivots_won.append(pivot_html)

#     closed_lost1 = dftf1.loc[dftf1['Selling Stage'] == lose]
#     closed_lost2 = dftf2.loc[dftf2['Selling Stage'] == lose]

#     merged_lost = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Selling Team'])
#     if not merged_lost.empty:
#         aggregated = merged_lost.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated.columns = ['Timeframe 1', 'Timeframe 2']
#         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
#                                             "closed_lost_team11.png", 
#                                             "Closed Lost by Selling Team (in USD)")
#         if chart_file:
#             charts.append(chart_file)
#         if pivot_html:
#             pivots_won.append(pivot_html)

#     merged_lost_seller = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Seller Name'])
#     if not merged_lost_seller.empty:
#         aggregated_seller = merged_lost_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
#         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None, 
#                                             "closed_lost_seller11.png", 
#                                             "Closed Lost by Seller (in USD)")
#         if chart_file:
#             charts.append(chart_file)
#         if pivot_html:
#             pivots_won.append(pivot_html)

#     sum_won1 = closed_won1['Recurring ACV (USD)'].sum() + closed_won2['Recurring ACV (USD)'].sum()
#     return pivots_won, charts, sum_won1



# def compare_two(dftf1,dftf2,win,lose):
#     closed_won1 = dftf1.loc[dftf1['Selling Stage'] == win]
#     closed_won2 = dftf2.loc[dftf2['Selling Stage'] == win]

#     merged_won = pd.merge(closed_won1, closed_won2, how='outer', on=['Selling Team'])
#     if not merged_won.empty:
#         aggregated = merged_won.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated.columns = ['Timeframe 1', 'Timeframe 2']  
        
#         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
#                                             "closed_won_team11.png", 
#                                             "Closed Won by Selling Team (in USD)")
#         charts = [chart_file] if chart_file else []
#         pivots_won = [pivot_html] if pivot_html else []
#     else:
#         charts = []
#         pivots_won = []

#     merged_won_seller = pd.merge(closed_won1, closed_won2, how='outer', on=['Seller Name'])
#     if not merged_won_seller.empty:
#         aggregated_seller = merged_won_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
        
#         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None, 
#                                             "closed_won_seller11.png", 
#                                             "Closed Won by Seller (in USD)")
#         if pivot_html and chart_file:
#             pivots_won.append(pivot_html)
#             charts.append(chart_file)


#     closed_lost1 = dftf1.loc[dftf1['Selling Stage'] == lose]
#     closed_lost2 = dftf2.loc[dftf2['Selling Stage'] == lose]

#     merged_lost = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Selling Team'])
#     if not merged_lost.empty:
#         aggregated = merged_lost.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated.columns = ['Timeframe 1', 'Timeframe 2']  
        
#         pivot_html, chart_file = create_pc2(aggregated, "Selling Team", None, 
#                                             "closed_lost_team11.png", 
#                                             "Closed Lost by Selling Team (in USD)")
#         charts = [chart_file] if chart_file else []
#         pivots_won = [pivot_html] if pivot_html else []
#     else:
#         charts = []
#         pivots_won = []

#     merged_lost_seller = pd.merge(closed_lost1, closed_lost2, how='outer', on=['Seller Name'])
#     if not merged_lost_seller.empty:
#         aggregated_seller = merged_lost_seller.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
#         aggregated_seller.columns = ['Timeframe 1', 'Timeframe 2']
        
#         pivot_html, chart_file = create_pc2(aggregated_seller, "Seller Name", None, "closed_lost_seller11.png", "Closed Lost by Seller (in USD)")
#         if pivot_html and chart_file:
#             pivots_won.append(pivot_html)
#             charts.append(chart_file)
#     sum_won1= closed_won1['Recurring ACV (USD)'].sum() + closed_won2['Recurring ACV (USD)'].sum()

 
#     return pivots_won, charts, sum_won1










@app.route ("/")
def home():
   return render_template('home.html')


@app.route("/help", methods=["GET","POST"])
def help():
   return render_template('help.html')


@app.route("/index", methods=["GET","POST"])
def index():
   return render_template('index.html')

@app.route("/noresults", methods=["GET","POST"])
def noresults():
   return render_template('noresults.html')


@app.route("/upload", methods=["POST"])
def upload_file():
   if 'file' not in request.files:
       flash('No file uploaded')
       return redirect(request.url)
  
  
   file=request.files['file']


   if file.filename=='':
       flash('No selected file')
       return redirect(request.url)
  
   filename=secure_filename(file.filename)
   file_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
   file.save(file_path)


   return redirect(url_for('choose', filename=filename))
@app.route("/choose/<filename>", methods=["GET","POST"]) 
def choose(filename):
   if request.method=="POST":
       if request.form.get("option")=="One Timeframe":
           return redirect(url_for('one_route', filename=filename))
       elif request.form.get("option")=="Two Timeframes":
           return redirect(url_for('enter_analysis_params', filename=filename))
      
   return render_template('choose.html', filename=filename)
   #return redirect(url_for('enter_analysis_params', filename=filename))
   #return redirect(url_for('enter_analysis_params'))
#@app.route('/enter_params/<filename>', methods=['POST', 'GET']) 


@app.route("/one_route/<filename>")
def one_route(filename):
   return render_template('analyze1.html', filename=filename)


@app.route("/enter_params/<filename>")
def enter_analysis_params(filename):
   return render_template('analyze.html', filename=filename) 


@app.route('/analyze1/<filename>', methods=['POST'])
def analyze1(filename):
   file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  
   if not os.path.exists(file_path):
       flash('File not found. Please upload the file again.')
       return redirect(url_for('noresults'))


   try:
       dataFrameOriginal = pd.read_excel(file_path)
       oppID = request.form.get('oppID')
       dataFrameOriginal.drop_duplicates(subset=[oppID], keep='first',  inplace=True)
       dataFrameOriginal['Created Date'] = pd.to_datetime(dataFrameOriginal['Created Date'], errors='coerce')
       dataFrameOriginal['Date Closed'] = pd.to_datetime(dataFrameOriginal['Date Closed'], errors='coerce')
      
       timeframe1_1 = request.form.get('timeframe1_1')
       timeframe1_2 = request.form.get('timeframe1_2')
      
      
       if timeframe1_1 and timeframe1_2 :
           dftf1 = dataFrameOriginal.loc[
               (dataFrameOriginal['Created Date'] >= timeframe1_1) &
               (dataFrameOriginal['Created Date'] <= timeframe1_2)]
           #file=dftf1.to_excel('Clean_Sorted.xlsx')
       else:
           flash ('Timeframe inputs required')
           return redirect(url_for('one_route', filename=filename))
          
       win_stage = request.form.get('win_stage', type=int)
       lose_stage = request.form.get('lose_stage', type=int)
      
       pivots_won, charts, sum_won1 = just_one(dftf1, win_stage, lose_stage)
       return render_template('results.html', results=pivots_won, charts=charts, sum_won1=sum_won1)
  
   except Exception as e:
       flash(f"Error during analysis: {e}")
       return redirect(url_for('noresults'))




@app.route('/analyze/<filename>', methods=['POST'])
def analyze(filename):
   file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  
   if not os.path.exists(file_path):
       flash('File not found. Please upload the file again.')
       return redirect(url_for('noresults'))


   try:
   
       dataFrameOriginal = pd.read_excel(file_path)
       oppID = request.form.get('oppID')
       dataFrameOriginal.drop_duplicates(subset=[oppID], keep='first',  inplace=True)
       dataFrameOriginal['Created Date'] = pd.to_datetime(dataFrameOriginal['Created Date'], errors='coerce')
       dataFrameOriginal['Date Closed'] = pd.to_datetime(dataFrameOriginal['Date Closed'], errors='coerce')
      
  
       timeframe1_1 = request.form.get('timeframe1_1')
       timeframe1_2 = request.form.get('timeframe1_2')
       timeframe2_1 = request.form.get('timeframe2_1')
       timeframe2_2 = request.form.get('timeframe2_2')
  
       if timeframe1_1 and timeframe1_2 and timeframe2_1 and timeframe2_2:
           dftf1 = dataFrameOriginal.loc[
               (dataFrameOriginal['Created Date'] >= timeframe1_1) &
               (dataFrameOriginal['Created Date'] <= timeframe1_2)]
           dftf2 = dataFrameOriginal.loc[
               (dataFrameOriginal['Created Date'] >= timeframe2_1) &
               (dataFrameOriginal['Created Date'] <= timeframe2_2)]
        #    file=dftf1.to_excel('Clean_Sorted.xlsx')
        #    file2=dftf2.to_excel('Clean_Sorted.xlsx')
          
       win_stage = request.form.get('win_stage', type=int)
       lose_stage = request.form.get('lose_stage', type=int)

       pivots_won, charts, sum_won1 = compare_two(dftf1, dftf2, win_stage, lose_stage)
       return render_template('results.html', results=pivots_won, charts=charts, sum_won1=sum_won1)

   except Exception as e:
       flash(f"Error during analysis: {e}")
       return redirect(url_for('noresults'))
  
@app.route('/static/charts/<filename>')
def serve_chart(filename):
   return send_from_directory(app.config['CHARTS_FOLDER'],filename)
@app.route('/pivot', methods=['GET','POST'])
def resultsp():
    return render_template('resultsp.html')

# @app.route('/downlaod')
# def downloadExcel():
#     root_path = "path_to_your_file"
#     filename = "your_file_name.xlsx"
#     file_path = os.path.join(root_path, filename)
#     return send_file(file_path)


if __name__=="__main__":
   app.run(debug=True, port= 5001)