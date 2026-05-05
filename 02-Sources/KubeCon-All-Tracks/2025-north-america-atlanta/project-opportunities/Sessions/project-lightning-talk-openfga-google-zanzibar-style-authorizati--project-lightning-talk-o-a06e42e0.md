---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: ["Tyler Nix", "Product Manager"]
sched_url: https://kccncna2025.sched.com/event/27d4i/project-lightning-talk-openfga-google-zanzibar-style-authorization-made-developer-friendly-tyler-nix-product-manager
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenFGA%3A+Google+Zanzibar+Style+Authorization+Made+Developer-Friendly+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: OpenFGA: Google Zanzibar Style Authorization Made Developer-Friendly - Tyler Nix, Product Manager

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: United States / Atlanta
- Speakers: Tyler Nix, Product Manager
- Schedule: https://kccncna2025.sched.com/event/27d4i/project-lightning-talk-openfga-google-zanzibar-style-authorization-made-developer-friendly-tyler-nix-product-manager
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenFGA%3A+Google+Zanzibar+Style+Authorization+Made+Developer-Friendly+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: OpenFGA: Google Zanzibar Style Authorization Made Developer-Friendly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4i/project-lightning-talk-openfga-google-zanzibar-style-authorization-made-developer-friendly-tyler-nix-product-manager
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenFGA%3A+Google+Zanzibar+Style+Authorization+Made+Developer-Friendly+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4xZqSO1OGSc
- YouTube title: Project Lightning Talk: OpenFGA: Google Zanzibar Style Authorization Made Developer-Fri... Tyler Nix
- Match score: 1.021
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-openfga-google-zanzibar-style-authorization-mad/4xZqSO1OGSc.txt
- Transcript chars: 4952
- Keywords: authorization, organization, folders, permissions, zanzibar, access, control, essentially, policy, object, folder, relate, documents, google, developer, centralized, written, incubating

### Resumo baseado na transcript

I uh work for Octa as a product manager overseeing the Open FGA project. I'm going to talk to you this morning about why Open FGA is the developer friendly way of doing authorization in your application. Um and then specifically in the security and compliance space uh we join other kind of authorization um projects such as open policy agent which you heard about before and and keycloak but we do things just slightly differently and I'll talk to you about that in a second.

### Excerpt da transcript

Hello everyone. My name is Tyler Nick. Tyler Nicks. I uh work for Octa as a product manager overseeing the Open FGA project. I'm going to talk to you this morning about why Open FGA is the developer friendly way of doing authorization in your application. So, Open FGA is a centralized authorization system built for developers. It's based on a concept called relationshipbased access control. And it's kind of a mesh between RO based access control and attribute-based access control. And it's inspired by a paper written by Google which they call Zanzibar. And so Zanzibar is their internal authorization system that they built for all their applications uh at scale. And essentially what we did is we took that paper and kind of the good things about it and then packaged it up into an open-source project that any developer would be able to use. But before I get into it, I have something really exciting to share. As of nine days ago, Open FGA has graduated from a sandbox project into a incubating project. So thank you We're really excited about this.

Back in uh September of 2022 when Octa donated the Open FGA to the CNCF, um this is something that we've always been building towards and so uh it's a big milestone for us. We also uh by doing that kind of join a highly selective group of incubating projects. It's 36 of them. Um and then specifically in the security and compliance space uh we join other kind of authorization um projects such as open policy agent which you heard about before and and keycloak but we do things just slightly differently and I'll talk to you about that in a second. Um open FGA is maintained by octa and graphana. There's also a lot of adopters that contribute to the project. So, some kind of names that you might know is uh Canonical and Docker, Headspace and and GoDaddy. And there's actually a lot of others, but uh due to their legal teams not allowing them to uh put their logo on this slide, uh they are unnamed. I wanted to call out though five specific ones. We just wanted to say a big thank you to Graphana and Docker, Aicap, and Zuplo and Reed AI.

they uh they were gracious to be interviewed by the CNCF uh during the due diligence process of of the incubation. So we just thank you for that. Um now really quick uh you need to have two things in order for open FGA to be able to evaluate a uh authorization policy. The first one is what we call an authorization model. So right here you'll see that we are defining an organization and you de
