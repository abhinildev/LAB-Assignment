from scipy.stats import chi2_contingency
data = [[207, 282, 241],
        [234, 242, 232]]
stat, p, dof, expected = chi2_contingency(data)
if p<0.5:
    print("The hyphothesis is rejected")
else:
    print("The hypothesis is accepted")