---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Johan Tordsson", "Elastisys AB"]
sched_url: https://kccnceu2021.sched.com/event/iE4e/compliance-beyond-security-a-cloud-native-gdpr-implementation-experience-johan-tordsson-elastisys-ab
youtube_search_url: https://www.youtube.com/results?search_query=Compliance+Beyond+Security%3A+a+Cloud+Native+GDPR+Implementation+Experience+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Compliance Beyond Security: a Cloud Native GDPR Implementation Experience - Johan Tordsson, Elastisys AB

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: Virtual / Virtual
- Speakers: Johan Tordsson, Elastisys AB
- Schedule: https://kccnceu2021.sched.com/event/iE4e/compliance-beyond-security-a-cloud-native-gdpr-implementation-experience-johan-tordsson-elastisys-ab
- Busca YouTube: https://www.youtube.com/results?search_query=Compliance+Beyond+Security%3A+a+Cloud+Native+GDPR+Implementation+Experience+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Compliance Beyond Security: a Cloud Native GDPR Implementation Experience.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4e/compliance-beyond-security-a-cloud-native-gdpr-implementation-experience-johan-tordsson-elastisys-ab
- YouTube search: https://www.youtube.com/results?search_query=Compliance+Beyond+Security%3A+a+Cloud+Native+GDPR+Implementation+Experience+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9DRAZez-UhE
- YouTube title: Compliance Beyond Security: a Cloud Native GDPR Implementation Experience - Johan Tordsson
- Match score: 0.986
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/compliance-beyond-security-a-cloud-native-gdpr-implementation-experien/9DRAZez-UhE.txt
- Transcript chars: 19976
- Keywords: privacy, compliance, security, native, european, personal, collect, protection, regulations, information, technologies, availability, particular, however, longer, europe, transfer, similar

### Resumo baseado na transcript

hi i'm yuan tortron i'm cto and co-founder of elasticis we're a swedish cncf member training partner and service provider and he was a creator on kubernetes distribution i also have a spare time job as standard faculty in computer science where i try to make microservices a bit more self-driving because we want self-driving cars and they want simplified use of i.t i've been researching and teaching distributed systems since the dark ages of soap-based web services and i do remember vividly when amazon web service introduced a fourth

### Excerpt da transcript

hi i'm yuan tortron i'm cto and co-founder of elasticis we're a swedish cncf member training partner and service provider and he was a creator on kubernetes distribution i also have a spare time job as standard faculty in computer science where i try to make microservices a bit more self-driving because we want self-driving cars and they want simplified use of i.t i've been researching and teaching distributed systems since the dark ages of soap-based web services and i do remember vividly when amazon web service introduced a fourth size vm today i'm going to share some of the experience that we had in elasticity helping various companies who wanted to embrace cloud-native technology and kubernetes while still operating a heavily regulated business sector so the title of my talk is compliance beyond security let me elaborate a bit on that it is well understood that in order to comply with various regulations you need a solid information security program and in fact there has been multiple talks in previous cube cons on this topic including quite a few stories about how to use search meshes to achieve end-to-end encryption across all your microservices i have nothing on service measures but there's more to compliance than that and today i want to bring attention to certain aspects of compliance that goes beyond traditional security or qui require you to take a different approach to security so traditional information security standards such as iso 27001 and sock2 focus a lot on topics such as confidentiality integrity and availability this so-called cia triad more recent regulations such as the european data protection regulation gdpr and the much inspired california consumer privacy act focus on a different aspect data privacy and end user rights to their data to illustrate some of these needs for the regulation let's do a mine experience considered a scenario where you're running an online service and one of you your users requests to unregister how do you do that well removing a user that's pretty straightforward we delete the corresponding record from our database or data stores or even perhaps just mark that particular user as removed because hey after all we hope that that user might change his or her mind and come back as user however if our user instead requests to be forgotten this is a much trickier question returning to our database example it is clearly not sufficient just to mark this particular user as removed without actually removing that re
