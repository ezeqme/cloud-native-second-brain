---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability"]
speakers: ["Vasudev Bongale", "LinkedIn"]
sched_url: https://kccncna2025.sched.com/event/27FVw/making-application-rollouts-observable-actionable-and-boring-vasudev-bongale-linkedin
youtube_search_url: https://www.youtube.com/results?search_query=Making+Application+Rollouts+Observable%2C+Actionable+and+Boring+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Making Application Rollouts Observable, Actionable and Boring - Vasudev Bongale, LinkedIn

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Atlanta
- Speakers: Vasudev Bongale, LinkedIn
- Schedule: https://kccncna2025.sched.com/event/27FVw/making-application-rollouts-observable-actionable-and-boring-vasudev-bongale-linkedin
- Busca YouTube: https://www.youtube.com/results?search_query=Making+Application+Rollouts+Observable%2C+Actionable+and+Boring+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Making Application Rollouts Observable, Actionable and Boring.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVw/making-application-rollouts-observable-actionable-and-boring-vasudev-bongale-linkedin
- YouTube search: https://www.youtube.com/results?search_query=Making+Application+Rollouts+Observable%2C+Actionable+and+Boring+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8QS3hmsDjNE
- YouTube title: Making Application Rollouts Observable, Actionable and Boring - Vasudev Bongale, LinkedIn
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/making-application-rollouts-observable-actionable-and-boring/8QS3hmsDjNE.txt
- Transcript chars: 26518
- Keywords: rollout, application, failure, platform, rollouts, deployment, status, message, failures, reason, understand, change, failed, condition, observable, actionable, making, observability

### Resumo baseado na transcript

I'm here to talk about uh my topic making application rollouts observable, actionable and boring. Uh and I'm super excited to be here as this is my first time speaking at Coupon. Bob on the other hand who governs the platform reliability is interested to understand the overall platform health. when you enter the world of Kubernetes uh the Kubernetes is always converging you answering these questions bit becomes a bit more trickier because Kubernetes is declarative and always converging. That means you need to get data from like look up YAML files, look up events, look up logs and imagine doing this thousands of engineers doing the scratch investigation all the time. At LinkedIn, we use Kubernetes as the building blocks of our platform and on top of that we have custom resources that the developers interact on daily basis.

### Excerpt da transcript

Nice to see you all. I'm here to talk about uh my topic making application rollouts observable, actionable and boring. Uh before I begin, I want to introduce a little bit about myself. Uh hello everyone. Uh I'm Vasuv. I am based off of San Francisco Bay Area. Uh and I'm super excited to be here as this is my first time speaking at Coupon. Um outside work, I love biking. Uh I explore some Bay Area hills and I love playing pickle ball as well. At LinkedIn I'm a software engineer on the concrete infrastructure team which supports all of LinkedIn engineers. Uh my focus has been in the past two years building a Kubernet LinkedIn's Kubernetes platform that serves the stateless applications uh with focus on observability, reliability and mainly developer experience. The compute infrastructure layer itself comprises of 500,000 servers. 500,000 servers running 3,000 applications inside 1.5 million containers. And these applications are changing at the rate of 50,000 rollouts a week. When we look at closely how is the platform being utilized, there are mainly two personas which are beneficiaries of this platform.

Uh, meet Alice, who's an application developer at LinkedIn who focuses on building application features. Uh, meet Bob. He's a platform engineer who builds and operates the platform that runs these applications. When Alice develops new code and deploys it to production, they typically have these questions. Hey, I just put a new piece of code. A new version is built. It's deployed to production. Did it succeed? or if not why it did not succeed and what can I do about it. Bob on the other hand who governs the platform reliability is interested to understand the overall platform health. So the typical questions are how's the platform doing? Are the rollout succeeding? That might be a great measure in specifically in the perspective application rollouts. But here's the tricky part. when you enter the world of Kubernetes uh the Kubernetes is always converging you answering these questions bit becomes a bit more trickier because Kubernetes is declarative and always converging. So that means when you change the desired state it is going to continuously reconcile forever until that desired state is met.

This translate into a fact that there is no native notion of hey there is a roll out done. This is the final state or a terminal state that you can take a next step forward from here. In other words, if ARIS asked a simple question, I click deploy on some UI and di
