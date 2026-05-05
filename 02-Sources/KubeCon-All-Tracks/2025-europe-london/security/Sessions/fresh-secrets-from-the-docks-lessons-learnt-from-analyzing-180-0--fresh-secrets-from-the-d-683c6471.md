---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["Security"]
speakers: ["Guillaume Valadon", "GitGuardian"]
sched_url: https://kccnceu2025.sched.com/event/1txFh/fresh-secrets-from-the-docks-lessons-learnt-from-analyzing-180000-public-dockerhub-images-guillaume-valadon-gitguardian
youtube_search_url: https://www.youtube.com/results?search_query=Fresh+Secrets+From+the+Docks%3A+Lessons+Learnt+From+Analyzing+180%2C000+Public+DockerHub+Images+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Fresh Secrets From the Docks: Lessons Learnt From Analyzing 180,000 Public DockerHub Images - Guillaume Valadon, GitGuardian

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United Kingdom / London
- Speakers: Guillaume Valadon, GitGuardian
- Schedule: https://kccnceu2025.sched.com/event/1txFh/fresh-secrets-from-the-docks-lessons-learnt-from-analyzing-180000-public-dockerhub-images-guillaume-valadon-gitguardian
- Busca YouTube: https://www.youtube.com/results?search_query=Fresh+Secrets+From+the+Docks%3A+Lessons+Learnt+From+Analyzing+180%2C000+Public+DockerHub+Images+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Fresh Secrets From the Docks: Lessons Learnt From Analyzing 180,000 Public DockerHub Images.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFh/fresh-secrets-from-the-docks-lessons-learnt-from-analyzing-180000-public-dockerhub-images-guillaume-valadon-gitguardian
- YouTube search: https://www.youtube.com/results?search_query=Fresh+Secrets+From+the+Docks%3A+Lessons+Learnt+From+Analyzing+180%2C000+Public+DockerHub+Images+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2r92tTuFYg8
- YouTube title: Fresh Secrets From the Docks: Lessons Learnt From Analyzing 180,000 Public Dock... Guillaume Valadon
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/fresh-secrets-from-the-docks-lessons-learnt-from-analyzing-180-000-pub/2r92tTuFYg8.txt
- Transcript chars: 24759
- Keywords: secrets, docker, secret, layers, images, config, github, repositories, million, obviously, called, scanning, actually, indeed, attackers, number, identify, create

### Resumo baseado na transcript

I scanned indeed 50 million images, a bit more than on the title, so I did some homework uh on the way to the conference. uh you might know um a tool that I'm working on Scrappy which is a Python library dedicated to um um sending and receiving um u packets packet in Python and um these days I'm doing security research for GitGuardian. They're scraping website for um in the past weeks attackers have been looking for secrets in GitHub action logs with great success. I want to behave as I did in the past as a pentester or doing offensive security. Um in security like in many other fields uh we have frameworks uh to define what we do. Um however there's another problem that's when you use a keyword the docker web search only return 10,000 results.

### Excerpt da transcript

I'm really happy to be here today. Thank you for being here with me. I've been in the all and I've seen a lot of people leaving. So, thanks a lot. First, owe you an apology. There's a typo in the title. I scanned indeed 50 million images, a bit more than on the title, so I did some homework uh on the way to the conference. Who am I? I'm G, French uh French guy. Used to be a network guy. uh you might know um a tool that I'm working on Scrappy which is a Python library dedicated to um um sending and receiving um u packets packet in Python and um these days I'm doing security research for GitGuardian. GitG Guardian that's a French company uh which is doing secret detection so at first obviously in Git and GitHub but not only so that's a bit disturbing uh not only in in in in code but do we do that in messaging systems we do that in uh things like Slack uh and our goal is to help customer identify secrets and remediate two weeks ago we released a report called the secrets pro report In this report, it's just let's say um uh a summary of the the discovery we do like every day with secrets.

The crazy crazy world. One of the information we like in this report is uh the fact that people tend to leak more secrets in private repositories that in public ones. So it tends to indicate that when people feel safe, they will arcode secrets. You can get it online. Uh it's free. There is no payw wall, no no address. If you want to play with the product, it's also free. So you can just create an account, plug your uh GitLab instance, GitHub instance, and it will start scanning the secrets for you. Uh but my goal today is indeed to to have a look at um what can attackers do with secrets. Um in the news, attackers are looking for secrets in many things like PIP packages. They're scraping website for um in the past weeks attackers have been looking for secrets in GitHub action logs with great success. it seemed that they managed to hack into Coinbase or at least some Coinbase dependencies. Um that's my focus today. I want to behave as I did in the past as a pentester or doing offensive security. So what can attackers do with secrets?

Um in security like in many other fields uh we have frameworks uh to define what we do. One of them is attack that's a way to define attacker attack path. So today we'll target counter registries in that case docker up. We start with valid credentials and these are not valid in the sense that they're default. You don't need credential to talk to
