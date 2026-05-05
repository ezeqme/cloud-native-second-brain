---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Application + Delivery"
themes: ["GitOps Delivery", "SRE Reliability"]
speakers: ["Edidiong Asikpo", "Ambassador Labs"]
sched_url: https://kccnceu2023.sched.com/event/1Hyb8/telepresence-case-studies-from-first-experience-to-fast-feedback-at-scale-edidiong-asikpo-ambassador-labs
youtube_search_url: https://www.youtube.com/results?search_query=Telepresence+Case+Studies%3A+From+First+Experience+to+Fast+Feedback+at+Scale+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Telepresence Case Studies: From First Experience to Fast Feedback at Scale - Edidiong Asikpo, Ambassador Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Application + Delivery]]
- Temas: [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Edidiong Asikpo, Ambassador Labs
- Schedule: https://kccnceu2023.sched.com/event/1Hyb8/telepresence-case-studies-from-first-experience-to-fast-feedback-at-scale-edidiong-asikpo-ambassador-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Telepresence+Case+Studies%3A+From+First+Experience+to+Fast+Feedback+at+Scale+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Telepresence Case Studies: From First Experience to Fast Feedback at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyb8/telepresence-case-studies-from-first-experience-to-fast-feedback-at-scale-edidiong-asikpo-ambassador-labs
- YouTube search: https://www.youtube.com/results?search_query=Telepresence+Case+Studies%3A+From+First+Experience+to+Fast+Feedback+at+Scale+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Hcm_elRpizo
- YouTube title: Telepresence Case Studies: From First Experience to Fast Feedback at Scale - Edidiong Asikpo
- Match score: 0.981
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/telepresence-case-studies-from-first-experience-to-fast-feedback-at-sc/Hcm_elRpizo.txt
- Transcript chars: 30337
- Keywords: remote, development, telepresence, cluster, application, environment, changes, running, actually, production, laptop, change, voting, developer, traffic, request, intercept, always

### Resumo baseado na transcript

all right um hello and welcome to this talk my name is I currently work as a senior developer Advocate at Ambassador Labs I am also a scientific Ambassador and you most often times find me writing building or sharing knowledge with people in The Tech Community I go by DD codes on all my social media platforms my name is Didion can be hard to pronounce so people call me DD but in case you can't pronounce it video DJ is fine um so on all my social media

### Excerpt da transcript

all right um hello and welcome to this talk my name is I currently work as a senior developer Advocate at Ambassador Labs I am also a scientific Ambassador and you most often times find me writing building or sharing knowledge with people in The Tech Community I go by DD codes on all my social media platforms my name is Didion can be hard to pronounce so people call me DD but in case you can't pronounce it video DJ is fine um so on all my social media platforms I go by DD codes except LinkedIn which is a combination of my first and last name asico so in this talk I'm going to share several case studies on how the cncf tool telepresence has enabled Cloud native companies to cut books before production I celebrate their inner Dev Loop and improve their developer experience this case studies are based off three companies culture code which are the creators of the things app voice flow and a fintech company you opted not to share their names just like most companies the development teams of these companies had certain kubernetes challenges that they wanted to fix or improve to improve their development workflow take things for instance like I mentioned this is an application created by the team at culture code things enables you to plan your day manage projects and make real progress towards your goals the development thing the development team at things uses kubernetes in AWS they have multiple services and they also have multiple managed databases and if you work with Cloud native applications you know that most often than not they always comprise of so many microservices and most times this microservices work interdependently and communicate with each other to achieve larger business goals and because of this multi-directional Services service communication it's always best to test your local code changes against the services and external dependencies they rely on before pushing into production because you want to ensure that it's going to work as expected when you eventually push it and of course this can be quite challenging you deal with things like limited resources inconsistent data between production and non-production environment and even managing distinct configuration for separate environments for the culture code team one of the things that really struggled with was the inconsistency between their Dev environment and production environment they would make a code change tested with the setup they had and assume everything is going to work as expect
