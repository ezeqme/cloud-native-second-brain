---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Clément Nussbaumer", "PostFinance"]
sched_url: https://kccnceu2026.sched.com/event/2CW3D/banking-on-reliability-cloud-native-sre-practices-in-financial-services-clement-nussbaumer-postfinance
youtube_search_url: https://www.youtube.com/results?search_query=Banking+on+Reliability%3A+Cloud+Native+SRE+Practices+in+Financial+Services+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Banking on Reliability: Cloud Native SRE Practices in Financial Services - Clément Nussbaumer, PostFinance

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Clément Nussbaumer, PostFinance
- Schedule: https://kccnceu2026.sched.com/event/2CW3D/banking-on-reliability-cloud-native-sre-practices-in-financial-services-clement-nussbaumer-postfinance
- Busca YouTube: https://www.youtube.com/results?search_query=Banking+on+Reliability%3A+Cloud+Native+SRE+Practices+in+Financial+Services+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Banking on Reliability: Cloud Native SRE Practices in Financial Services.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3D/banking-on-reliability-cloud-native-sre-practices-in-financial-services-clement-nussbaumer-postfinance
- YouTube search: https://www.youtube.com/results?search_query=Banking+on+Reliability%3A+Cloud+Native+SRE+Practices+in+Financial+Services+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pgmQ8YqyjUQ
- YouTube title: Banking on Reliability: Cloud Native SRE Practices in Financial Services - Clément Nussbaumer
- Match score: 0.962
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/banking-on-reliability-cloud-native-sre-practices-in-financial-service/pgmQ8YqyjUQ.txt
- Transcript chars: 26864
- Keywords: server, connection, requests, request, cluster, perhaps, implemented, application, actually, tomcat, slo, servers, thought, traffic, ingress, seconds, engineext, thanks

### Resumo baseado na transcript

Thanks for joining me to this session on reliability topics in a Swiss bank. Let's start with a few words about me and some context about the company I work for. you set an objective on one of your services and then you can use a tool like for example slo to help you define all the metrics recording rules um that you need to really implement this objective and monitor it uh in the long uh cubers it is a demon set which does uh continuous health checks in your cluster so it runs on all nodes and it performs a series of checks. So servicing API server DNS IP we have the neighboring neighborhood check and the idea of this check is that cubers is going to query all the other cubner spots to to know the state. neighbors if I go back to the linear order it appears randomly distributed And through this hash ring the the interesting thing about that is the metrics are going to be stable.

### Excerpt da transcript

Well, welcome everyone. Thanks for joining me to this session on reliability topics in a Swiss bank. I'm glad you're here to this afternoon. And uh let's get started. Let's start with a few words about me and some context about the company I work for. So I'm a Swiss systems engineer. I work for Post Finance, a relatively large system systemic bank in Switzerland. I happen to live on a farm, which is a pretty fun fact. We are where I try to implement lots of cloud native solutions for my wife and her associates. I play music and I'm a young father and uh for post finance it is a as I said quite big bank in Switzerland where we operate on prem kubernetes clusters vanilla kubernetes clusters I talked about it last year uh we were migrating from cubadium to talos it's still an ongoing progress and um yeah we we are building most of the solutions around kubernetes by by ourselves as you will see in this talk and yeah we are a bank. For us, a failed request means that someone is at an ATM trying to to to get some money or trying to pay in a shop and it doesn't work.

Perhaps there is retry. Per is some delay. Perhaps they are stuck there for 5 minutes. So, we really cannot afford to have failed requests. That's really quite bad on our customers. So, that's why we have uh implemented lots of solutions around uh site reliability engineering principles. And the first one I want to cover is service level service level objective. So back then we didn't have any SLO service level objective. We just had some feedback from our users. So the application developers for the finance for example or other applications for the bank or the other developer of the platform and it was like oh well this morning did you did you see it was pretty slow. K9S feel slow. I did a cube cut get it took perhaps two minutes to to to get a response and this was temporary and we basically ignored it because if you do not have really a a target you just ignore the the bad uh services that you could get. So this was pretty subjective and we ignored those uh this bad quality of service and so someone suggested that we take a look at service level objectives which is something really well defined in the Google's sur book and which I will not cover in too many details here but the idea is that if you provide a service I really encourage you to define an objective for that service for example for the API server one of one of our objectives is the availability we want that less than.1% of the request
