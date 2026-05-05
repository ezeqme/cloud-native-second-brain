---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Bob Walker", "Octopus Deploy"]
sched_url: https://kccnceu2025.sched.com/event/1txAN/how-we-progressively-deliver-changes-to-kubernetes-using-canary-deployments-and-feature-flags-bob-walker-octopus-deploy
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Progressively+Deliver+Changes+To+Kubernetes+Using+Canary+Deployments+and+Feature+Flags+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How We Progressively Deliver Changes To Kubernetes Using Canary Deployments and Feature Flags - Bob Walker, Octopus Deploy

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Bob Walker, Octopus Deploy
- Schedule: https://kccnceu2025.sched.com/event/1txAN/how-we-progressively-deliver-changes-to-kubernetes-using-canary-deployments-and-feature-flags-bob-walker-octopus-deploy
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Progressively+Deliver+Changes+To+Kubernetes+Using+Canary+Deployments+and+Feature+Flags+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How We Progressively Deliver Changes To Kubernetes Using Canary Deployments and Feature Flags.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAN/how-we-progressively-deliver-changes-to-kubernetes-using-canary-deployments-and-feature-flags-bob-walker-octopus-deploy
- YouTube search: https://www.youtube.com/results?search_query=How+We+Progressively+Deliver+Changes+To+Kubernetes+Using+Canary+Deployments+and+Feature+Flags+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zZ7bDPZMCqY
- YouTube title: How We Progressively Deliver Changes To Kubernetes Using Canary Deployments and Featur... Bob Walker
- Match score: 0.996
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-we-progressively-deliver-changes-to-kubernetes-using-canary-deploy/zZ7bDPZMCqY.txt
- Transcript chars: 28508
- Keywords: customers, feature, deploy, canary, deployments, functionality, always, self-hosted, production, interface, deployment, features, little, instances, toggles, started, octopus, anyone

### Resumo baseado na transcript

Um, this is probably the most people I've spoken to in terms of a conference. Uh, so I'm definitely going to mess up at some point, so please forgive me if I do. Now the goals for this particular session today is I want to provide you with solutions that you can apply in your day-to-day based on the some of the challenges that we faced and this is just working under the assumption that your use case is fairly similar. I will show you like a couple of screenshots, but it will make sense in that uh but really but you will have to understand what we're doing uh just to understand our challenges. So a little bit about our architecture in case anyone's curious, we leverage cell-based architecture. And the big reason why we did this is this allows us to scale up and down the compute resources per customer because we have some customers who need to do tens of deployments per day and we have others that need to do thousands of deployments per day.

### Excerpt da transcript

I'm going to go ahead and get started. Um, this is probably the most people I've spoken to in terms of a conference. Uh, so I'm definitely going to mess up at some point, so please forgive me if I do. Uh, my name is Bob Walker. I'm the field CTO at Octopus Deploy, and I'm really excited to be here because I get a chance to talk to you about how we, as a company, now progressively deliver changes to our customers who are hosted on Kubernetes using a Canary style deployment as well as feature flags. Now, before I jump into that, just a little bit about me as people continue to stream in. Uh, first up, you might be seeing field CTO. Um, almost everyone blows right through the field part of that and just thinks I'm a CTO. I'm not a CTO. I am in still an individual contributor. I can't set the direction of a company. I can't hire anybody. I really can't tell anyone to do anything. But uh my job as a field CTO is to go out and speak at different conferences, uh put together different thought pieces, talk to different customers, uh do a whole bunch of other different fun stuff like that.

Uh but I did achieve a very important distinction last year where scammers are now using me for fishing attacks to my own company. So that's great. Um all my contact information is up there. Uh that QR code sends you to my LinkedIn profile. If you want to connect with me, please feel free to go ahead and do that. Now, you can probably tell by my accent that I'm not from around here. I live in Omaha, Nebraska. Um, if you haven't heard of Omaha, most people haven't. I don't blame you. Uh, we just went over a million people. Uh, that's where it is on the map. I live there with my wife and we have two cats and a dog. And if you're curious about what on earth does Nebraska look like, uh, that's what it looks like. Um, when I'm not spending time with my wife or my pets or at conferences or talking to customers, I'm going to be out on the bike. Uh, so we have a lot of rolling hills. Doesn't really show up super well in that picture. Uh, but it's a lot of farmland and a lot of big open air. And I promise we do have cities.

Um, that's just an old railsto trails conversion trail. So while I've worked at a number of different companies, in fact, I started off as a developer way back in the early days ofnet. And as much as I'd love to tell you about that story, primarily this story is going to focus in on my experience within Octopus Deploy. Now the goals for this particular session today
