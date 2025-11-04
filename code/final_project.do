*Food-Health Data analysis

clear all
set more off

*Task 1
*Set working directory 
*Import the data
cd "C:\Users\Sagatova_Gulnaz\Desktop\coding\"
import delimited "C:\Users\Sagatova_Gulnaz\Downloads\food-health.csv"
describe
summarize

*Task 5
* Replace missing values with empty values
* Convert numeric text variables to real numbers
* Fill numeric missing values with their column means
ds, has(type string)
local strvars `r(varlist)'
local strvars `r(varlist)'
foreach v of local strvars {
    replace `v' = "" if `v' == "NA" | `v' == "?" | `v' == " "
}
destring bp_diastolic total_cholesterol hdl weight height ldl bmi, replace ignore(".")
summarize bp_diastolic, meanonly
replace bp_diastolic = r(mean) if missing(bp_diastolic)
summarize total_cholesterol, meanonly
replace total_cholesterol = r(mean) if missing(total_cholesterol)
summarize hdl, meanonly
replace hdl = r(mean) if missing(hdl)
summarize weight, meanonly
replace weight = r(mean) if missing(weight)
summarize height, meanonly
replace height = r(mean) if missing(height)
summarize ldl, meanonly
replace ldl = r(mean) if missing(ldl)
summarize bmi, meanonly
replace bmi = r(mean) if missing(bmi)

*Task 6
* Keep normal BMI range
* Select key columns
* Create new ratios
keep if bmi >= 18.5 & bmi <= 30
keep weight height bmi total_cholesterol hdl ldl heart_risk
keep weight height bmi total_cholesterol hdl ldl heart_risk
generate w_h_ratio = weight / height
generate log_cholesterol = ln(total_cholesterol)

*Task 7
*Save cleaned data
save "food-health-cleaned.dta", replace
export delimited using "food-health-cleaned.csv", replace

*Task 8
*Create a summary statistics table
summarize

*Task 9 and 10
*Create a graph
*Save a graph
histogram bmi, bin(30) title("Distribution of BMI")
graph export "bmi_histogram.png", replace

twoway scatter total_cholesterol bmi, title("BMI vs Total Cholesterol") xtitle("BMI") ytitle("Total Cholesterol")
graph export "bmi_cholesterol_scatter.png", replace

*The end. 
*Thank you for your attention!