---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Ashley Davis", "Tim Ramlot", "Venafi"]
sched_url: https://kccncna2024.sched.com/event/1hovY/best-friends-keep-no-secrets-going-secretless-with-cert-manager-ashley-davis-tim-ramlot-venafi
youtube_search_url: https://www.youtube.com/results?search_query=Best+Friends+Keep+No+Secrets%3A+Going+Secretless+with+cert-manager+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Best Friends Keep No Secrets: Going Secretless with cert-manager - Ashley Davis & Tim Ramlot, Venafi

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Ashley Davis, Tim Ramlot, Venafi
- Schedule: https://kccncna2024.sched.com/event/1hovY/best-friends-keep-no-secrets-going-secretless-with-cert-manager-ashley-davis-tim-ramlot-venafi
- Busca YouTube: https://www.youtube.com/results?search_query=Best+Friends+Keep+No+Secrets%3A+Going+Secretless+with+cert-manager+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Best Friends Keep No Secrets: Going Secretless with cert-manager.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hovY/best-friends-keep-no-secrets-going-secretless-with-cert-manager-ashley-davis-tim-ramlot-venafi
- YouTube search: https://www.youtube.com/results?search_query=Best+Friends+Keep+No+Secrets%3A+Going+Secretless+with+cert-manager+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VbCtDF8qlWA
- YouTube title: Best Friends Keep No Secrets: Going Secretless with cert-manager - Ashley Davis & Tim Ramlot, Venafi
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/best-friends-keep-no-secrets-going-secretless-with-cert-manager/VbCtDF8qlWA.txt
- Transcript chars: 29485
- Keywords: manager, certificate, certificates, secretless, secret, driver, actually, account, solution, workload, questions, secrets, talking, tokens, question, request, issuer, running

### Resumo baseado na transcript

hello welcome everyone um today we will be talking about how to go secretless with SE manager so my name is Tim this is Ash we're both SE management maintainers and we both work for Fifi which recently has been acquired by C Arc so let's start with s manager what is s manager in one sentence SE manager is the best way to get x59 certificates if you're running any kind of workload in kubernetes basically CT manager uses the kubernetes API so you can use the API to we configured in the fult pki setup and in the common names or in the uh s we will actually see the DNS name example.com so that's the full demo that's how everything works and that's how you can secretless secretless request certificates using search a terminal obviously that's what the demo was but there's quite a lot of important steps in that the key thing is that authentication is important right it's it's easy to set up so manager to get certificates for you but you have to think

### Excerpt da transcript

hello welcome everyone um today we will be talking about how to go secretless with SE manager so my name is Tim this is Ash we're both SE management maintainers and we both work for Fifi which recently has been acquired by C Arc so let's start with s manager what is s manager in one sentence SE manager is the best way to get x59 certificates if you're running any kind of workload in kubernetes basically CT manager uses the kubernetes API so you can use the API to interact with CT manager to request certificates and then it will automatically provision those certificates for you and make sure that they are renewed in time so you don't have any outages applications that then get these certificates they can use them to do server and client authentication and basically as you see in the diagram search manager kind of acts as a as a intermediary between your application and a certificate Authority it requests certificates for the application and then it places the obtain certificates close to the application so it can be used by the application but C is more than just a technical solution it's actually a whole community of people who are interested in pki who are interested in kubernetes controllers that kind of fun stuff and I'm very honored to announce here for the first time um at Cube that se manager has reached the cncf graduated status if you don't know what it is it's basically a label to recognize the quality of the project the quality of the community and also all the effort that we put in the e in the project um I would like to thank all the contributors all the users and also the the rest of the maintainers for ofert manager I think it has been an amazing journey to get to this point and I mean this just one step in this journey we'll continue working on the project we'll continue growing all these stats that you see on the screen and we'll continue improving the project on that note if you want to contribute if you're if you're feeling inspired by this talk um please reach out reach out to us you can use this codes to learn more um we're always open to new people who are interested in this space who are interested in controllers um so feel free to join us so then for the second part of the talk or of the title of the talk secretless basically if we're talking about secretless we mean by that the fact that no secrets are shared across machine in your system so no secrets are shared over the wire um an easy way to explain what secretless is is by expl
