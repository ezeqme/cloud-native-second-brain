---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Moritz Johner", "Form3"]
sched_url: https://kccnceu2023.sched.com/event/1HyYQ/protecting-your-crown-jewels-with-external-secrets-operator-moritz-johner-form3
youtube_search_url: https://www.youtube.com/results?search_query=Protecting+Your+Crown+Jewels+with+External+Secrets+Operator+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Protecting Your Crown Jewels with External Secrets Operator - Moritz Johner, Form3

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Moritz Johner, Form3
- Schedule: https://kccnceu2023.sched.com/event/1HyYQ/protecting-your-crown-jewels-with-external-secrets-operator-moritz-johner-form3
- Busca YouTube: https://www.youtube.com/results?search_query=Protecting+Your+Crown+Jewels+with+External+Secrets+Operator+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Protecting Your Crown Jewels with External Secrets Operator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYQ/protecting-your-crown-jewels-with-external-secrets-operator-moritz-johner-form3
- YouTube search: https://www.youtube.com/results?search_query=Protecting+Your+Crown+Jewels+with+External+Secrets+Operator+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=upwIlUHkDf8
- YouTube title: Protecting Your Crown Jewels with External Secrets Operator - Moritz Johner, Form3
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/protecting-your-crown-jewels-with-external-secrets-operator/upwIlUHkDf8.txt
- Transcript chars: 33579
- Keywords: secrets, secret, operator, external, provider, cluster, access, pretty, resource, little, question, account, management, sequence, provide, manager, generate, application

### Resumo baseado na transcript

everyone can you hear me cool awesome yeah welcome everyone to my talk uh protecting your crown jewels with external Secrets operator um my name is Jonah I am one of the maintainers of the external Secrets operator project and from my day job I work as a senior software engineer at form 3 where I work in the platform compute containers team and we built the kubernetes infrastructure for all the of the other application teams across three different Cloud providers and on-premises which is a huge task yeah Secrets out and they store them as a kubernetes secret resource so then applications can pick them up as a file environment Etc there were many projects which were like not so popular popular like maybe 30 stars on GitHub 50 stars on GitHub and

### Excerpt da transcript

everyone can you hear me cool awesome yeah welcome everyone to my talk uh protecting your crown jewels with external Secrets operator um my name is Jonah I am one of the maintainers of the external Secrets operator project and from my day job I work as a senior software engineer at form 3 where I work in the platform compute containers team and we built the kubernetes infrastructure for all the of the other application teams across three different Cloud providers and on-premises which is a huge task yeah there's also Lookouts on Gustavo which are here today there in the first row and we also have a booth in the cncf project Pavilion in hall five so if you have any questions afterwards I don't have the time to do a demo today if you have questions afterwards you can feel free feel free to just talk here or afterwards just in the booth um so without further Ado um we are here to raise some awareness that this project exists because I don't know if people are aware of it and I would like to do a quick show of hands and ask you like who of you is aware that this project exists and I have a rough idea what it does cool awesome that's quite a few people um awesome and who of you guys are actually using it way less but still a couple of people awesome so um if you have the time feel free to come by our booth we'd like to learn more about how you use it with what kind of stuff you struggle with and how we can improve so um feel free to come by um so what I've I have for the agenda for today is first and foremost I would like to do I give you a rough overview What secrets management is what kind of the challenges you have typically typically when you want to implement sequence management this will be roughly about 10-ish minutes um for those watching the vods that you're already familiar with it just skip the 10 minutes um after that I'll talk about external sequence operator everyone else who's familiar with thickness management feel free to pass out and I'm gonna catch you later so what is sequence management and why should you care in every organization we have some sort of Secrets or credentials that allow members of your organization to access internal services that could be a monitoring system that could be production access to a database there could be like a lot of different things so these are the kinds of Secrets we're talking about mostly credentials username password combinations API Keys all that kind of stuff and that's important and you should care a
