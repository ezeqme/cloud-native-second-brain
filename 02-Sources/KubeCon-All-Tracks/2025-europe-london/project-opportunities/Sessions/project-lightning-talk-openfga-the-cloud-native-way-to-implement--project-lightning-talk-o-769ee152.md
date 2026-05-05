---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Andres Aguiar", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcwm/project-lightning-talk-openfga-the-cloud-native-way-to-implement-fine-grained-authorization-andres-aguiar-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenFGA%3A+The+Cloud+Native+Way+to+Implement+Fine+Grained+Authorization+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: OpenFGA: The Cloud Native Way to Implement Fine Grained Authorization - Andres Aguiar, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Andres Aguiar, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcwm/project-lightning-talk-openfga-the-cloud-native-way-to-implement-fine-grained-authorization-andres-aguiar-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenFGA%3A+The+Cloud+Native+Way+to+Implement+Fine+Grained+Authorization+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: OpenFGA: The Cloud Native Way to Implement Fine Grained Authorization.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwm/project-lightning-talk-openfga-the-cloud-native-way-to-implement-fine-grained-authorization-andres-aguiar-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenFGA%3A+The+Cloud+Native+Way+to+Implement+Fine+Grained+Authorization+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ohS-ibtvQWw
- YouTube title: Project Lightning Talk: OpenFGA: The Cloud Native Way to Implement Fine Grained Aut... Andres Aguiar
- Match score: 0.983
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-openfga-the-cloud-native-way-to-implement-fine/ohS-ibtvQWw.txt
- Transcript chars: 5657
- Keywords: authorization, access, control, organization, application, implement, define, integrations, graphana, parent, folder, relationship, google, simple, defining, tupils, folders, permissions

### Resumo baseado na transcript

I'm a product manager at Octa and I'm being I'm a maintainer in Open FGA. You're going to use it if you want to implement authorization in an application like for example same way or similar way you can use open policy agent and it's based on a concept called relationship based access control that you can see as an evolution of role based access control and attribute-based access control. And uh these are the things the community is building around open FGA right demos providers operators more SDKs API gateways integrations framework integrations IDPS ID integrations all of those built by the community these are some of the adopters that are using open FGA So you can go to the website and start learning how to use it if you want it.

### Excerpt da transcript

Hi everyone. So my name is Andres Agar. I'm a product manager at Octa and I'm being I'm a maintainer in Open FGA. Open FJ is an authorization system for developers. You're going to use it if you want to implement authorization in an application like for example same way or similar way you can use open policy agent and it's based on a concept called relationship based access control that you can see as an evolution of role based access control and attribute-based access control. It's inspired by a research paper published by Google a few years ago where they describe a system they call Google Zanzibar which is the way they found to implement authorization in a way that is generic enough for any use case at Google and they defined a way you can do that define a model to implement it for any application and also build it to scale to their scale. What we did is we created a server, a set of tools, APIs, SDKs, CLIs, ID integrations to make it simple for you to integrate in your applications. We're in the sandbox stage.

We apply for incubation. We are in the second line of projects to be evaluated for incubation and it's maintained mostly by octa with help from graphana labs. How open FJ works? You need two things to work with open FGA. First is defining what we call an authorization model where you're going to describe the entities that are relevant when making authorization decisions. In this case for a very simple multi-tenant role-based access control where you have organizations with your tenants and for each of them you can have admins or members and we're saying you can edit if you're an admin or you can view if you're a member of an admin. In addition of the model, we need to instantiate that model with data. And we call them those tupils, relationship tupils. In this case, we're saying that Maria is a member of the ACME organization and an is an admin an admin on the ACME organization. And then we can define and with that data and the organization, the model and the tupils uh we can write it using the the right API.

This is using the the Go SDK. We have SDKs for a lot of platforms. We store that data in a database. We support SQLite progress and my SQL currently. And then whenever we want to know if a user cover from an action and a resource, we ask we call the check API. In this case, Mary can edit a specific organization. So this was very simple, but let's make it a little more complex. The nice thing about relationship based access control is that
