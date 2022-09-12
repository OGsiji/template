# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta
import os



# # Local libraries
# from time_series_analysis import plot_states, plot_countries
# from daily_counts import plot_daily_count_states, plot_daily_count_countries
# from create_case_maps import plot_usa_case_map, plot_global_case_map
# from helper import Mode

WIDTH = 210
HEIGHT = 297

TEST_DATE = "21/08/22"



def create_title(TEST_DATE, pdf):
  # Unicode is not yet supported in the py3k version; use windows-1252 standard font
  pdf.set_font('Arial', 'B', 24)  
  pdf.ln(60)
  pdf.write(5, f"Strategy Analytics Daily Report")
  pdf.ln(10)
  pdf.set_font('Arial', 'B', 16)

  pdf.write(4, f'{TEST_DATE}')
  pdf.ln(5)

def create_analytics_report(filename="macro_report.pdf"):
    pdf = FPDF() # A4 (210 by 297 mm)

    ''' First Page '''
    pdf.add_page()
    pdf.image("Images/letter_head.png", 0, 0, WIDTH)
    create_title(TEST_DATE, pdf)

    #   plot_usa_case_map("./tmp/usa_cases.png", day=day)
    #   prev_days = 250
    
    #   plot_states(states, days=prev_days, filename="./tmp/cases.png", end_date=day)
    #   plot_states(states, days=prev_days, mode=Mode.DEATHS, filename="./tmp/deaths.png", end_date=day)

    pdf.image("Images/cover-letter.png", 10, 90, WIDTH-20,150)
    pdf.image("Images/letter_tail.png",0,275, WIDTH)


    '''Second Page'''

    pdf.add_page()
    # Remember to always put one of these at least once.
    pdf.set_font('Times','',10.0) 
    
    # Effective page width, or just epw
    epw = pdf.w - 2*pdf.l_margin
    
    # Set column width to 1/4 of effective page width to distribute content 
    # evenly across table and page
    col_width = epw/4
    
    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.
    

    data1 = [
    ["Market", "MTD", "YTD",],
    ["SPX",   "-1.76%", "-14.86%",],
    ["NDX",  "-2.53%",  "-22.68%",],
    ["DJI",   "-1.71%",  "-11.15%",],
    ]

    Growth = "0.0%"

    data2 = [
    ["Fund", "MTD" ,"YTD",],
    ["Defensive" , "-0.76%", "-3.49%",],
    ["Growth" ,"-0.07%", f"{Growth}",],
    ["Supertrend","+5.45%","+5.45%",],
    ["Discretionary","+0.39%","-7.52%",],
    ["Aggregate","+0.11%","-2.43%",],
    ]

    
    # Document title centered, 'B'old, 14 pt
    pdf.set_font('Times','B',14.0) 
    pdf.cell(epw, 0.0, 'Market', align='C')
    pdf.cell(epw, 0.0, ' ', align='C')
    pdf.set_font('Times','',10.0) 
    pdf.ln(10)
    
    # Text height is the same as current font size
    th = pdf.font_size
    
    for row in data1:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 2*th, str(datum), border=1)
    
        pdf.ln(2*th)
    
    # Line break equivalent to 4 lines
    pdf.ln(4*th)
    
    pdf.set_font('Times','B',14.0) 
    pdf.cell(epw, 0.0, 'Fund', align='C')
    pdf.set_font('Times','',10.0) 
    pdf.ln(10)
    
    # Here we add more padding by passing 2*th as height
    for row in data2:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 2*th, str(datum), border=1)
    
        pdf.ln(2*th)



    #pdf.ln(10)
    #pdf.cell(5) 
    #pdf.write(5, f"The readings today showed that defensive gave the best returns with a return of 5.6% and which beats the market baseline of 0.5%")
    #pdf.cell(20, 10, "The readings today showed that defensive gave the best returns with a score of 25.6% and we can expect similar growth on all other platforms before this year runs out", 0, 1, 'C')
    # pdf.set_font('Arial', 'B', 16)
    # pdf.ln(10)
    # pdf.cell(WIDTH/2-50) 
    # pdf.cell(20, 10, "Description of Strategies", 0, 0, 'C')
    #pdf.cell(20, 10, '', 0, 2, 'C')

 
    #pdf.image("Images/stock_heat_map.png",  20, 180, WIDTH-30, 40)
    pdf.image("Images/desc_stra.png", 2, 130, WIDTH,120)
    pdf.image("Images/quat_ret.png", 2, 220, WIDTH,120)
    #pdf.image("Images/bottom_up.png", WIDTH/2, 180, WIDTH/2-10,60)




    ''' Third Page '''
    pdf.add_page()

      # Set font
    pdf.set_font('Arial', 'B', 16)
    # Move to 8 cm to the right
    pdf.ln(10)
    pdf.cell(50)
    # Centered text in a framed 20*10 mm cell and line break
    pdf.cell(20, 10, 'Top_down Results', 0, 0, 'C')

    pdf.image("Images/bottom_up.png", 2, 50, WIDTH,90)
    
    pdf.ln(150)
    pdf.cell(50)
    pdf.cell(20, 10, 'Bottom_up Results', 0, 0, 'C')
    pdf.image("Images/Top_down.png", 2, 180, WIDTH,90)

    ''' Fourth Page '''
    pdf.add_page()
    # Remember to always put one of these at least once.
    pdf.set_font('Times','',10.0) 
    
    # Effective page width, or just epw
    epw = pdf.w - 2*pdf.l_margin
    
    # Set column width to 1/4 of effective page width to distribute content 
    # evenly across table and page
    col_width = epw/4
    
    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.
    

  

    data1 = [
    ["Fund", "Risk Model Results"],
    ["Defensive" , "76%"],
    ["Growth" ,"25%"],
    ["Supertrend","49%"],
    ["Discretionary","31%"],
    ["Aggregate","22%",],
    ]

    
    # Document title centered, 'B'old, 14 pt
    pdf.set_font('Times','B',14.0) 
    pdf.cell(epw, 0.0, 'Risk Model Results', align='C')
    pdf.cell(epw, 0.0, ' ', align='C')
    pdf.set_font('Times','',10.0) 
    pdf.ln(10)
    
    # Text height is the same as current font size
    th = pdf.font_size
    for row in data1:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 2*th, str(datum), border=1)
    
        pdf.ln(2*th)
    
    # Line break equivalent to 4 lines
    pdf.ln(4*th)
    




    #pdf.ln(10)
    #pdf.cell(5) 
    #pdf.write(5, f"The readings today showed that defensive gave the best returns with a return of 5.6% and which beats the market baseline of 0.5%")
    #pdf.cell(20, 10, "The readings today showed that defensive gave the best returns with a score of 25.6% and we can expect similar growth on all other platforms before this year runs out", 0, 1, 'C')
    # pdf.set_font('Arial', 'B', 16)
    # pdf.ln(10)
    # pdf.cell(WIDTH/2-50) 
    # pdf.cell(20, 10, "Description of Strategies", 0, 0, 'C')
    #pdf.cell(20, 10, '', 0, 2, 'C')

 
    #pdf.image("Images/stock_heat_map.png",  20, 180, WIDTH-30, 40)
    pdf.image("Images/Supertrend.png", 2, 70, WIDTH,90)
    pdf.image("Images/Growth.png", 2, 140, WIDTH,90)
    pdf.image("Images/Defensive.png", 2, 220, WIDTH,90)
    #pdf.image("Images/bottom_up.png", WIDTH/2, 180, WIDTH/2-10,60)

    
    ''' Fifth Page '''
    pdf.add_page()

    # Set font
    pdf.set_font('Arial', 'B', 16)
    # Move to 8 cm to the right
    pdf.cell(5)
    # Centered text in a framed 20*10 mm cell and line break
    pdf.cell(20, 10, 'Evergreen Returns vs Index', 0, 0, 'L')

    pdf.cell(WIDTH/2-10)
    pdf.cell(20, 10, "Portfolio stocks  history", 0, 0, 'L')

    pdf.image("Images/output.png", 5, 30, WIDTH/2-10, 90)
    pdf.image("Images/stocks_type.png", WIDTH/2, 30, WIDTH/2-10, 130)
    
    # pdf.ln(130)
    # pdf.cell(WIDTH/2-10)
    # pdf.cell(20, 10, "", 0, 0, 'C')
    # pdf.cell(20, 10, '', 0, 2, 'C')


    pdf.image("Images/sectors_correlate.png",  2, 150, WIDTH-10, 160)


    #'''Third Page '''
    # pdf.add_page()
    #    # Set font
    # pdf.set_font('Arial', 'B', 16)
    # # Move to 8 cm to the right
    # pdf.cell(5)
    # # Centered text in a framed 20*10 mm cell and line break
    # pdf.cell(20, 10, 'Distribution of annual return', 0, 0, 'L')

    # pdf.cell(WIDTH/2-20)
    # pdf.cell(20, 10, "Distribution of total_pl", 0, 0, 'L')

    # pdf.image("Images/output2.png", 5, 30, WIDTH/2-10, 90)
    # pdf.image("Images/output3.png", WIDTH/2, 20, WIDTH/2-10, 90)
    
    
    # pdf.ln(130)
    # pdf.cell(WIDTH/2-10)
    # pdf.cell(20, 10, "Stocks baseline trading metrics", 0, 0, 'C')
    # pdf.cell(20, 10, '', 0, 2, 'C')


    # pdf.image("Images/output_main.png",  5, 150, WIDTH-30, 150)


    ''' Fourth Page '''
    pdf.add_page()
     

    pdf.image("Images/4 horse_men.png", 5, 20, WIDTH/2-10)
    pdf.image("Images/high_bet.png", WIDTH/2, 20, WIDTH/2-10)


    pdf.image("Images/Val_gr.png", 5, 110, WIDTH/2-10)
    pdf.image("Images/small_cap.png", WIDTH/2, 110, WIDTH/2-10)

    pdf.ln(180)
    pdf.cell(WIDTH/2-10)
    pdf.cell(20, 10, "Daily Market Sentiment", 0, 0, 'C')
    pdf.cell(20, 10, '', 0, 2, 'C')

    pdf.image("Images/sentiment.png",  20, 200, WIDTH-30, 90)


    #pdf.image("Images/SPY.png", 5, 200, WIDTH/2-10)
    #pdf.image("./tmp/deaths3.png", WIDTH/2, 200, WIDTH/2-10)
    pdf.add_page()
    

    pdf.image("Images/Annual_returns.png", 5, 20, WIDTH-20)
    #pdf.image("Images/strategy_results.png", 5, 130, WIDTH/2-10)
    pdf.image("Images/SPY.png", 5, 130, WIDTH-10,150)


    pdf.output(filename, 'F')




if __name__ == '__main__':
    create_analytics_report(filename="report.pdf")

    
