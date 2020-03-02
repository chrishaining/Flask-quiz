from app import db
from app.models import Topic, AnswerChoices, MultipleChoiceTopic


Topic.query.delete()
MultipleChoiceTopic.query.delete()

topic1 = Topic(question="What are virtual currencies and how do they work?", answer="Virtual currencies are electronic fiat currencies. They are very similar to traditional fiat currencies, but there is no physical currency (e.g. coin, paper, cheque). I'm not sure how they work.")
topic2 = Topic(question="What is the aim of an effective customer due diligence (CDD) programme and why is it important in combating money laundering and terrorist financing risks in the FinTech market?", answer="Effective CDD means that financial institutions know who their customers are and only banks with customers who have passed the CDD requirements. This in turn means that the financial institutions only bank with customers they trust: they do not bank with customers who cannot be trusted to operate legitimately. This therefore reduces the risk of the financial institution's services being used for financial crime and money laundering.")
topic3 = Topic(question="What are the money laundering/terrorist financing risks associated with the speed and mobility of some FinTech?", answer="Transactions can be conducted before a financial institution has had time to check that the transaction is legitimate. CDD can be more difficult - it can be easier to fake things, and harder to collect CDD documentation. FinTech products can bypass national boundaries, so it can be hard to know where money has really come from.")

topic4 = Topic(question="What is the FATF and how does its work apply to new technologies?", answer="Financial Action Task Force: I'm not sure how its work applies to new technologies. I'm guessing it will recommend controls be put in place.")

topic5 = Topic(question="What is meant by the term ‘cryptocurrency’ and why do cryptocurrencies present a challenge to the aims of financial integrity?", answer="I don't know the difference between a cryptocurrency and a virtual currency (if there is a difference). I'm not sure why they present a challenge to financial integrity - is it just because they are not owned by traditional financial institutions? Is it because they are complicated? Is it their volatility (in terms of value going up and down)? Is it because it can be hard to know who owns the currency, and where it comes from?")


topic6 = Topic(question="What is meant by the term risk-based approach (RBA) and what are the key risk factors to be considered when formulating a RBA relation to new payment methods?", answer="I actually don't know, even though the term has been used so frequently. My feeling is that there are differing interpretations, and that I've often heard two people talking about RBA but using different definitions.")


topic7 = Topic(question="Although low transaction limits may be an important factor in making new payment methods ‘low risk’ in respect of money laundering, the same products may still be useful for terrorist financiers. Why is this?", answer="the low cost of the transactions removes a barrier for making a high volume of payments. So, although an individual transaction might be low-value and thus low risk, a terrorist financier could make lots of low-value transactions that add up to a high value. This means that we really have a high risk of TF. Also, new payment methods mean it is relatively easy to split the TF activity between several different remitters and beneficiaries, making the true nature of the activity difficult to spot.")


topic8 = Topic(question="What are the two main categories of prepaid cards, and which is more susceptible to financial crime?", answer="")


topic9 = Topic(question="What is RegTech and how will it impact upon a firms approach to regulatory compliance?", answer="")

topic10 = Topic(question="What are centralised and decentralised virtual currencies and how do they differ. How do they tie in to convertible and non-convertible virtual currency?", answer="")

topic11 = Topic(question="What is network monitoring?", answer="Contextual or network monitoring is transaction monitoring in the context of a wider set of information about the customer or trade. Unit 4, p.63")

topic12 = Topic(question="How might blockchain be used in RegTech?", answer="Using the building blocks of blockchain would introduce a shared ledger to ensure that transactional activity within the chain can be monitored and adjusted in a more efficient way. Due to the shared nature of the ledger, a comprehensive database of client activity and background information would be available to all on the network. Unit 4, p. 64")


topic13 = Topic(question="How might blockchain be used in CDD?", answer="Blockchain allows this information to be shared through a unified platform with multiple service providers and also allows individual entities within the Blockchain to decide how much and what information they want shared between the multiple service providers they deal with. Unit 4, p. 65")


topic14 = Topic(question="", answer="")


topic15 = Topic(question="", answer="")



mult_choice1 = MultipleChoiceTopic(question="What is the time?", answer='Now', option_a="Then", option_b="Soon", option_c="Now", user_answer="Now")
mult_choice2 = MultipleChoiceTopic(question="What is the date?", answer='Today', option_a="Yesterday", option_b="Today", option_c="Tomorrow")
mult_choice3 = MultipleChoiceTopic(question="What is the year?", answer='This year', option_a="Last year", option_b="This year", option_c="Next year")


db.session.add(topic1)
db.session.add(topic2)
db.session.add(topic3)
db.session.add(topic4)
db.session.add(topic5)
db.session.add(topic6)
db.session.add(topic7)
db.session.add(topic8)
db.session.add(topic9)
db.session.add(topic10)

db.session.commit()


db.session.add(mult_choice1)
db.session.add(mult_choice2)
db.session.add(mult_choice3)
db.session.commit()

timey = Topic.query.all()
print(timey)

mults = MultipleChoiceTopic.query.all()
print(mults[0].option_d)
my_answer = mult_choice1.check_answer()
print(my_answer)
print(mult_choice1.outcome)