nosetests --with-cov --cov gobals
coverage report
coverage html -d covreport
cd covreport
index.html
cd ..


