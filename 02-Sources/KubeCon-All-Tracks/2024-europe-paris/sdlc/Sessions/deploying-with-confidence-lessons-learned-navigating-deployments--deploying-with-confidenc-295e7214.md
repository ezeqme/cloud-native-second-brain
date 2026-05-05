---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["GitOps Delivery"]
speakers: ["Stephanie Hingtgen", "Michael Mandrus", "Grafana Labs"]
sched_url: https://kccnceu2024.sched.com/event/1YeSY/deploying-with-confidence-lessons-learned-navigating-deployments-of-a-100-strong-development-team-stephanie-hingtgen-michael-mandrus-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Deploying+with+Confidence%3A+Lessons+Learned+Navigating+Deployments+of+a+100-Strong+Development+Team+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Deploying with Confidence: Lessons Learned Navigating Deployments of a 100-Strong Development Team - Stephanie Hingtgen & Michael Mandrus, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[GitOps Delivery]]
- País/cidade: France / Paris
- Speakers: Stephanie Hingtgen, Michael Mandrus, Grafana Labs
- Schedule: https://kccnceu2024.sched.com/event/1YeSY/deploying-with-confidence-lessons-learned-navigating-deployments-of-a-100-strong-development-team-stephanie-hingtgen-michael-mandrus-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Deploying+with+Confidence%3A+Lessons+Learned+Navigating+Deployments+of+a+100-Strong+Development+Team+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Deploying with Confidence: Lessons Learned Navigating Deployments of a 100-Strong Development Team.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSY/deploying-with-confidence-lessons-learned-navigating-deployments-of-a-100-strong-development-team-stephanie-hingtgen-michael-mandrus-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Deploying+with+Confidence%3A+Lessons+Learned+Navigating+Deployments+of+a+100-Strong+Development+Team+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XffdYT5SH6Y
- YouTube title: Deploying with Confidence: Lessons Learned Navigating Deployments of a 100-Strong Development Team
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/deploying-with-confidence-lessons-learned-navigating-deployments-of-a/XffdYT5SH6Y.txt
- Transcript chars: 26029
- Keywords: feature, toggle, developers, toggles, release, features, deploying, releases, channels, finally, recommend, internal, instances, deployment, manually, rolling, software, cost

### Resumo baseado na transcript

hello everyone thank you all so much for being willing to stay later on a Friday and talk about deployment practices so by a show of hands who here has had a bug that has made it to production that caused an incident okay yeah pretty much everyone now keep Your Hand raised if following that incident you thought hm that took a little bit longer to fix than I thought it should have okay yeah me too so I want to tell you about one specific time that ended

### Excerpt da transcript

hello everyone thank you all so much for being willing to stay later on a Friday and talk about deployment practices so by a show of hands who here has had a bug that has made it to production that caused an incident okay yeah pretty much everyone now keep Your Hand raised if following that incident you thought hm that took a little bit longer to fix than I thought it should have okay yeah me too so I want to tell you about one specific time that ended up sending us down a multiple year journey to improve our deployment practices this was a few years ago when we were deploying a new version to cloud and we had spent the morning manually building it then the afternoon manually deploying it and then bam alerts start firing escalations are coming in it turns out that the new feature that we had deployed had a problem that had more cascading effect on the system so the evening we spent rolling back the new version the next morning the Developers come in and they start working on a fix and we think we have one so again we spend the morning manually building it then the afternoon manually rolling it uh manually rolling it out and then bam more alerts start firing escalations are coming in it turns out that the fix worked slightly differently locally than it did in Cloud so again we manually roll it back at this point our users are understandably getting frustrated because with that release there had been bug fixes that some of them had been waiting for so understandably frustration was growing amongst the users the next morning the developers come in we figure out what the difference was between local and Cloud patch it ship it to cloud and finally the incident is over but we still had a multiple year journey ahead of us to improve our deployment practices so we're here to tell you about our journey and hopes that you all can get some better sleep while on call and your users can experience a more Smooth release process us so hi I am Stephanie hinin and I am a senior software engineer at gra Labs hi I'm am Michael mandas I'm also a senior software engineer at graffo labs and this is our guide to sane and safe Cloud deployments so let's look back at where we were at the beginning of that incident at the time we had our priority towards on-prem releases so we were building our on-prem releases and then shipping those manually to Cloud now those manual shipments to Cloud were pretty tedious and so we only did those monthly and since we only did those monthly and ha
