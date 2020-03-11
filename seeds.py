from app import db
from app.models import Topic, Resource


Topic.query.delete()
Resource.query.delete()

topic1 = Topic(question="What are virtual currencies and how do they work?", answer="Digital, virtual or cryptocurrencies are created, bought and traded online in exchange for both virtual and actual goods and services. They are used in specific online marketplaces, linked to virtual worlds or social networks, and for online gambling and to purchase real goods and services. Virtual currency does not have legal tender status. It is a digital representation of value that can be digitally traded and functions as: * a medium of exchange\n * a unit of account\n * a store of value.")

topic2 = Topic(question="What is the aim of an effective customer due diligence (CDD) programme and why is it important in combating money laundering and terrorist financing risks in the FinTech market?", answer="An effective CDD programme must identify customers, verify the information they provide, monitor changes in account behaviour, highlight suspicious or unusual transactions and pinpoint the customer’s account for investigation and ultimately reporting suspicious activity if appropriate. \nEffective and robust CDD underpins AML and CFT programmes and is often where an institution will concentrate a large part of its efforts and resources.")

topic3 = Topic(question="What are the money laundering/terrorist financing risks associated with the speed and mobility of some FinTech?", answer="The nature of some FinTech means that it is possible for the user to conduct transactions without being in a fixed location, which makes detecting the movement of illicit activity much more difficult to detect.\n The high speed and versatility of FinTech lends itself well to the layering stage of the ‘traditional’ money laundering model. The removal of face-to-face interaction with bank cashiers means that anonymity becomes rife. For example, a criminal with internet access could easily move funds across multiple accounts in multiple jurisdictions in a matter of minutes.")

topic4 = Topic(question="What is the FATF and how does its work apply to new technologies?", answer="FATF is the international standard setter for measures to combat money laundering, terrorist financing and proliferation financing, and is arguably the most influential body working on the subject.\nIn 2006 and 2010, FATF produced reports on NPPS, focusing on the vulnerabilities to money laundering and terrorist financing found in the then emerging new businesses of the prepaid cards, mobile payments and Internet-based payment services (IPS) sectors.\nThe 2013 FATF report Guidance for a Risk Based Approach: Prepaid Cards, Mobile Payments and Internet-Based Payment Services built on the previous two reports, as well as providing guidance on implementing the risk- based approach and financial inclusion considerations.\nFATF has supplemented the 2013 guidance with two additional publications on virtual currencies. In June 2014, FATF published Virtual Currencies: Key Definitions and Potential AML/CFT Risks, which sought to build upon the 2013 NPPS report and suggested a framework for understanding and addressing AML/CFT risks. It also recognised the limitations of the 2013 NPPS paper, as it broadly addressed Internet-based payment systems and did not focus on virtual currencies nor address decentralised convertible virtual currencies. A year later, in June 2015, FATF published Guidance for a Risk Based Approach: Virtual Currencies which sought to address the gaps for virtual currency payments products and services (VCPPS).\nThe continued focus from FATF has remained, and their work alongside regulators reflects the change within this new industry. In June 2019, FATF issued further guidance for a Risk-Based Approach to Virtual Assets and Virtual Asset Service Providers. The increased use of virtual assets for money laundering and terrorist financing has led to the need for countries and providers to strengthen their controls. This additional guidance will help countries and virtual asset service providers understand their AML/CFT obligations, and effectively implement the FATF’s requirements as they apply to this sector. It also reflects changes within the sector, the risk is no longer centred on the firms that exchange fiat currency for virtual currency, but the broad spectrum of activities within the virtual asset space, including virtual-to-virtual transfers.")

topic5 = Topic(question="What is meant by the term ‘cryptocurrency’ and why do cryptocurrencies present a challenge to the aims of financial integrity?", answer="Cryptocurrency is a form of virtual currency that uses blockchain technology to hold transactions. Cryptocurrency is the token traded, and it is called cryptocurrency because cryptography is used to secure the validity of the entries on the blockchain.\nFinancial integrity is concerned with stopping the illicit flow of capital moved by, for example, organised criminals and tax evasion schemes, which ultimately divert enormous amounts of funds away from developing economies and into the hands of a few.\nWhether and how financial integrity and financial inclusion can be mutually beneficial is a question raised by the increased use of cryptocurrencies.\nCryptocurrency often targets customers who have been prevented from using traditional financial services, whether through poor financial history, inability to repay credit or a lack of formal identification.\nDue to the anonymity that convertible decentralised virtual currencies offer, the difficulties in carrying out proper identification of participants, virtual currency payment products and services (VCPPSs) are generally regarded as having a higher risk of money laundering and terrorist financing, therefore requiring enhanced measures.\nHowever, bringing the financially excluded and previously unbanked into the formal financial services sector can be complementary to the anti money laundering/combating the financing of terrorism (AML/CFT) objective, as it can help ensure that funds are moved through regulated and traceable channels.?")


topic6 = Topic(question="What is meant by the term risk-based approach (RBA) and what are the key risk factors to be considered when formulating a RBA relation to new payment methods?", answer="A risk-based approach means that firms ensure that their systems and controls are proportionate to their particular risks of financial crimes. Under a RBA, institutions should apply measures, systems and controls to safeguard the financial system that are appropriate to the level of risk posed by each product or client. \n The key risk factors to be considered when formulating a risk-based approach to new payments methods include:\n *product type\n*distribution channel\n*jurisdiction\n*customer type\n*volume and size of transactions.")


topic7 = Topic(question="Although low transaction limits may be an important factor in making new payment methods ‘low risk’ in respect of money laundering, the same products may still be useful for terrorist financiers. Why is this?", answer="the low cost of the transactions removes a barrier for making a high volume of payments. So, although an individual transaction might be low-value and thus low risk, a terrorist financier could make lots of low-value transactions that add up to a high value. This means that we really have a high risk of TF. Also, new payment methods mean it is relatively easy to split the TF activity between several different remitters and beneficiaries, making the true nature of the activity difficult to spot.\nThe official answer:\nLow transaction amounts that may deter money launderers might still be attractive for the purpose of terrorist financing, as this generally involves relatively small cash sums compared with those found in money laundering.")


topic8 = Topic(question="What are the two main categories of prepaid cards, and which is more susceptible to financial crime?", answer="Prepaid cards can be split into two broad categories: open-loop cards and closed-loop cards. By their nature, open-loop cards have a greater exposure to abuse by financial criminals because closed-loop cards have a limited negotiability or use.\nThis does not mean that there is no money laundering and terrorist financing risk associated with closed-loop prepaid cards. When closed-loop cards are used in financial crime, case studies show they are used as intermediary stores of value rather than as payment instruments.")


topic9 = Topic(question="What is RegTech and how will it impact upon a firms approach to regulatory compliance?", answer="RegTech can be defined as the use of technology to deliver regulatory requirements and compliance imperatives with speed, efficiency and accuracy. RegTech can be described as technology that provides ‘nimble, configurable, easy to integrate, reliable, secure and cost-effective’ regulatory solutions (Deloitte).\nThe use of RegTech will transform regulatory compliance by the automating of duties such as due diligence, using data that can be tailored to a firm’s risk-based approach, disrupting ineffective and outdated processes of regulation compliance by using artificial intelligence and machine learning. RegTech will change how due diligence practices are executed, how anti fraud measures work and how banks filter the wheat from the chaff when deciding whether to make a suspicious activity report.")

topic10 = Topic(question="What are centralised and decentralised virtual currencies and how do they differ. How do they tie in to convertible and non-convertible virtual currency?", answer="Centralised currencies are characterised by having a single administering authority. They are issued by the administrator, are subject to rules of use and are recorded on a central payment’s ledger. The value of the currency is either floating (determined by supply and demand) or pegged (whereby the value is either fixed by the administrator or is set to a real-world value, such as fiat currency).\nA decentralised virtual currency is authorised by its users whereby transactions take place on exchanges however there is no trusted third-party ledger. Decentralised virtual currency can be converted/exchanged for fiat currency and can be used across borders without restrictions.\nConvertible currencies can either be centralised or non-centralised, however, all non-convertible currencies are centralised.")

topic11 = Topic(question="What is network monitoring?", answer="Contextual or network monitoring is transaction monitoring in the context of a wider set of information about the customer or trade. Unit 4, p.63")

topic12 = Topic(question="How might blockchain be used in RegTech?", answer="Using the building blocks of blockchain would introduce a shared ledger to ensure that transactional activity within the chain can be monitored and adjusted in a more efficient way. Due to the shared nature of the ledger, a comprehensive database of client activity and background information would be available to all on the network. Unit 4, p. 64")

topic13 = Topic(question="How might blockchain be used in CDD?", answer="Blockchain allows this information to be shared through a unified platform with multiple service providers and also allows individual entities within the Blockchain to decide how much and what information they want shared between the multiple service providers they deal with. Unit 4, p. 65")


topic14 = Topic(question="Almost half the world's unbanked live in which countries? (name seven countries)", answer="China, India, Pakistan, Indonesia, Nigeria, Mexico and Bangladesh")


topic15 = Topic(question="How can technology change the exploitation of society by organised criminality?", answer="Financial crimes have data typologies that can be spotted if enough information can be analysed and machine learning tools can find such patterns.")


topic16 = Topic(question="New technologies present a new set of risks that firms must understand and mitigate, including which of the following?", answer="i) Digital evolution is fast but cultural change is slow. \nii) Data breaches degrade and destabilise the basic expectation that an individual's private information is not commoditised. \niii) Increasing reliance on interconnected systems increases the impact when these fail. \niv) Automation and new technology require forward-thinking governance mechanisms and operational controls.")


topic17 = Topic(question="A virtual asset provider, according to the FATF, is a natural or legal person not covered elsewhere under the Recommendations and provides which of the following on behalf of another legal or natural person?", answer="i) Exchange between virtual assets and fiat currency \n ii) Transfer of virtual assets \n iii) Custodian services for virtual assets")


topic18 = Topic(question="The concept of electronic money (e-money) was defined under which piece of European legislation?", answer="The Electronic Money Directive")


topic19 = Topic(question="How will FinTech force incumbent financial services firms adapt to meet the challenge of 'tech savvy' rivals and new entrants?", answer="i) Cultural change will be needed. \n ii) They will need to adapt hiring practices to attract 'tech talent'. \n iii) Branding will need to focus on the customer experience.")


topic20 = Topic(question="FinTech presents contradictions to be carefully considered because:", answer="it can be used to detect and prevent certain financial crimes but can be abused to perpetuate others")


topic21 = Topic(question="The initial phase of FinTech carries increased operational risk owing to:", answer="a lack of technical skills, shortage of expert staff and inadequate technology infrastructure")


topic22 = Topic(question="When can a system become vulnerable to financial crime?", answer="When controls are not tailored to the product and purpose")

topic22 = Topic(question="Neither regulators nor banks have been able to build a consistent and universally applicable approach to risk profiling and applying control mechanisms to new market entrants – with banks quite often treating them in the same way they would treat money service businesses.  What is the principal reason for this?", answer="The speed of market entry by FinTechs")


# topic22 = Topic(question="", answer="")


# topic22 = Topic(question="", answer="")


# topic22 = Topic(question="", answer="")


# topic22 = Topic(question="", answer="")


# topic22 = Topic(question="", answer="")


# topic22 = Topic(question="", answer="")





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
db.session.add(topic11)
db.session.add(topic12)
db.session.add(topic13)
db.session.add(topic14)
db.session.add(topic15)
db.session.add(topic16)
db.session.add(topic17)
db.session.add(topic18)
db.session.add(topic19)
db.session.add(topic20)
db.session.add(topic21)
db.session.add(topic22)



db.session.commit()

timey = Topic.query.all()
print(timey)
