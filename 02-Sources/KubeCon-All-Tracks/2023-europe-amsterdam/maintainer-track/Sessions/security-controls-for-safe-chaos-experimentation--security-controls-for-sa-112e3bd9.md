---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Raj Babu Das", "Umasankar Mukkara", "Harness"]
sched_url: https://kccnceu2023.sched.com/event/1HyUt/security-controls-for-safe-chaos-experimentation-raj-babu-das-umasankar-mukkara-harness
youtube_search_url: https://www.youtube.com/results?search_query=Security+Controls+for+Safe+Chaos+Experimentation+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Security Controls for Safe Chaos Experimentation - Raj Babu Das & Umasankar Mukkara, Harness

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Raj Babu Das, Umasankar Mukkara, Harness
- Schedule: https://kccnceu2023.sched.com/event/1HyUt/security-controls-for-safe-chaos-experimentation-raj-babu-das-umasankar-mukkara-harness
- Busca YouTube: https://www.youtube.com/results?search_query=Security+Controls+for+Safe+Chaos+Experimentation+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Security Controls for Safe Chaos Experimentation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyUt/security-controls-for-safe-chaos-experimentation-raj-babu-das-umasankar-mukkara-harness
- YouTube search: https://www.youtube.com/results?search_query=Security+Controls+for+Safe+Chaos+Experimentation+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=whCkvLKAw74
- YouTube title: Security Controls for Safe Chaos Experimentation - Raj Babu Das & Umasankar Mukkara, Harness
- Match score: 0.791
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/security-controls-for-safe-chaos-experimentation/whCkvLKAw74.txt
- Transcript chars: 27672
- Keywords: experiment, security, litmus, engineering, policy, network, experiments, access, account, execute, result, question, delegate, select, second, actually, create, introduced

### Resumo baseado na transcript

hi everyone good evening hope you are all having a great conference almost uh the end of second day thanks for making it um we have about uh 30 minutes so we will try to cover a general introduction of what this project is about and then the actual topic is also about security controls um so today we are talking about some security concentrations when you're doing Chaos engineering that that's the topic I'll go a little bit uh deep into it before we start a bit of introductions

### Excerpt da transcript

hi everyone good evening hope you are all having a great conference almost uh the end of second day thanks for making it um we have about uh 30 minutes so we will try to cover a general introduction of what this project is about and then the actual topic is also about security controls um so today we are talking about some security concentrations when you're doing Chaos engineering that that's the topic I'll go a little bit uh deep into it before we start a bit of introductions head of chaos engineering at harness I co-created this project litmus chaos in 2018 along with Karthik and few others um I continue to maintain this project so we have a team of a great line of Maintenance who are at Torrance right now and I have with me today Raj Das and one of the litmus maintain apart from this I am also a contributor to many projects like Evernote Prometheus and a few others yeah that's all about me thank you thank you all right um so I just really want to know a little bit about audience here how many of you are aware of chaos engineering or how many of you are using litmus okay thank you okay so that really means that you know it uh it's good to spend some time on um what is litmus why what's the journey right um but actually today's topic uh there were some questions hey you know um are you talking about uh security chaos engineering or security for chaos engineering right so that that so I just wanted to make it a bit clear here um chaos engineering for security is about running chaos experiments to assert that there are either security weaknesses or there are no security weaknesses right and security for chaos engineering is your anime doing Chaos engineering chaos experiments in your environment and you're making sure that you're doing it securely right what we are talking about is the second topic right today and towards the end I'll uh if time permits I'll cover uh in general you know if you want to run some security chaos experiments what are those and you know the the latest project in general is had to go there but I can talk to that some of those scenarios so what we talk today is um introduce litmus in general and some of the security challenges or considerations once you start implementing chaos engineering is a practice uh what are the security challenges and possible medications around that how to solve them um so what we do is we take each of those five or six examples and then my colleague here Raj will actually demonstrate how you would do tha
