---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Payal Godhani", "Oracle"]
sched_url: https://kccncna2025.sched.com/event/27FeJ/mission-abort-intercepting-dangerous-deletes-before-helm-hits-apply-payal-godhani-oracle
youtube_search_url: https://www.youtube.com/results?search_query=Mission+Abort%3A+Intercepting+Dangerous+Deletes+Before+Helm+Hits+Apply+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Mission Abort: Intercepting Dangerous Deletes Before Helm Hits Apply - Payal Godhani, Oracle

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Payal Godhani, Oracle
- Schedule: https://kccncna2025.sched.com/event/27FeJ/mission-abort-intercepting-dangerous-deletes-before-helm-hits-apply-payal-godhani-oracle
- Busca YouTube: https://www.youtube.com/results?search_query=Mission+Abort%3A+Intercepting+Dangerous+Deletes+Before+Helm+Hits+Apply+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Mission Abort: Intercepting Dangerous Deletes Before Helm Hits Apply.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FeJ/mission-abort-intercepting-dangerous-deletes-before-helm-hits-apply-payal-godhani-oracle
- YouTube search: https://www.youtube.com/results?search_query=Mission+Abort%3A+Intercepting+Dangerous+Deletes+Before+Helm+Hits+Apply+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9-IJHdVNgO4
- YouTube title: Mission Abort: Intercepting Dangerous Deletes Before Helm Hits Apply - Payal Godhani, Oracle
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/mission-abort-intercepting-dangerous-deletes-before-helm-hits-apply/9-IJHdVNgO4.txt
- Transcript chars: 15872
- Keywords: release, deployment, resource, cluster, balancer, particular, running, deleted, resources, production, customers, obviously, getting, framework, important, helmiff, information, critical

### Resumo baseado na transcript

I work uh for a deployment service and the topic for today is uh mission of bot intercepting dangerous deletes before helm hits apply. This is this topic and this talk is going to focus on how we can safeguard our kubernetes resources uh using a framework and prevent any seven or two incidents in production. It it doesn't come with any warnings and that is where this declarative trap sometimes becomes a huge problem in the production environment. deployment service person when we go and look at the logs we also see the same thing hey everything was everything is running as what it was supposed to run but still the service is down right so then We started looking in further into So the way this guardrails framework we have designed a framework specifically for this. Helm also works with a two-way release, but it doesn't query the live cluster state.

### Excerpt da transcript

My name is P Gdani. I'm from Oracle cloud infrastructure. I work uh for a deployment service and the topic for today is uh mission of bot intercepting dangerous deletes before helm hits apply. This is this topic and this talk is going to focus on how we can safeguard our kubernetes resources uh using a framework and prevent any seven or two incidents in production. So as for at least for Oracle uh our cloud regions are expanding rapidly. We are growing at a very rapid pace. We have more than 100 plus regions going on and we are going to add 50 more regions this year. Uh so one of the difficulties that SR has been facing is they are deploying 100 plus releases on on an everyday basis because they have a huge ground to cover. They have so many cloud regions to deploy to and along with the speed comes the trouble that there is a huge gap over there. So it becomes errorprone. One of the incidents that come to my mind is there was one particular incident where the S sur did as they were expected to do the routine deployments but what ended up happening was it did ended up deleting 18 load balancers in one go and it was for one of our multi-million dollar customers.

So you can understand the impact and the severity of this incident and as a result of it uh we had lot of seven calls going on and we we were trying to figure out how to resolve this what what went wrong because when the helm deployment went through it was successful. So let's take a look at what happened during that time when the S sur was trying to deploy that Helm release. uh during the deployment planning there were no warnings, no alarms that went off. The when the deployment got executed, it marked as successful. Nothing went wrong. Everything worked as it was supposed to. But soon after the alarm started firing up, the canaries turned green. Canaries turned red. And yes, then obviously those gruesome calls on what went wrong, how did it go wrong. For the record, it took us eight plus hours to get that service back up and running and obviously the multiple cars and everything comes along with it. So then in this particular case it was uh uh after a lot of debug we got to know that there was just one condition that got flipped by in one of the Helm charts due to which those 18 load balancers were wiped off completely just a single small mistake but to get to this level of debug and analysis it took us so long.

So then an very important question came to our mind that is there something that we
