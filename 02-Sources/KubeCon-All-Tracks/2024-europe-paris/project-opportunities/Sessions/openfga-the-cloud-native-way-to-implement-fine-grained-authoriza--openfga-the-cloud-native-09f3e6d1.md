---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["AI ML"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQij/openfga-the-cloud-native-way-to-implement-fine-grained-authorization-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=OpenFGA%3A+The+Cloud+Native+way+to+implement+Fine+Grained+Authorization+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# OpenFGA: The Cloud Native way to implement Fine Grained Authorization | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQij/openfga-the-cloud-native-way-to-implement-fine-grained-authorization-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=OpenFGA%3A+The+Cloud+Native+way+to+implement+Fine+Grained+Authorization+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre OpenFGA: The Cloud Native way to implement Fine Grained Authorization | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQij/openfga-the-cloud-native-way-to-implement-fine-grained-authorization-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=OpenFGA%3A+The+Cloud+Native+way+to+implement+Fine+Grained+Authorization+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=K7Me3OjFxJ0
- YouTube title: OpenFGA: The Cloud Native way to implement Fine Grained Authorization | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/openfga-the-cloud-native-way-to-implement-fine-grained-authorization-p/K7Me3OjFxJ0.txt
- Transcript chars: 6932
- Keywords: authorization, organization, define, permissions, folder, access, specific, document, relationship, control, simple, entities, member, policy, developers, details, action, managed

### Resumo baseado na transcript

okay so today I'm I'm going to talk about open fga and the and how it is helping different uh projects in the community and companies to implement fine grain authorization for the cloud natives applications I'm Andre SAR I'm a pro manager at OCTA and I lead the open fga project so open fga it's an authorization system for developers it's based on a concept called relationship based access control that you can see it as an evolution of role based access control and attribute based Access Control it's

### Excerpt da transcript

okay so today I'm I'm going to talk about open fga and the and how it is helping different uh projects in the community and companies to implement fine grain authorization for the cloud natives applications I'm Andre SAR I'm a pro manager at OCTA and I lead the open fga project so open fga it's an authorization system for developers it's based on a concept called relationship based access control that you can see it as an evolution of role based access control and attribute based Access Control it's inspired by a research paper that Google published a few years ago where they described how they implemented authorization internally in a way that it was flexible enough to address any of the use cases they have internally and also scale at the scale they need what I did is go we packaged those ideas with a server plus sdks apis and tooling to make it simple for developers to integrate this into your applications we are currently in the sandbox stage we are there we're there for a year and a half and the angu just applied for incubation four days ago say is there and right now this is surprising when I saw it but if you list all the projects by number of commits uh open fga in number eight which is awesome and so let's try to understand what open fga is so when you're modeling authorization with open fga okay you're going to do two things you're going to first Define what we call an authorization model where you're going to describe the entities that are relevant when you're making an authorization decision this is a very simple role based Access Control model that is kind of multitenant so the same user can have different roles in different organizations okay and and then we can say that if you are an admin you can edit the organization details or view them and if you're a member you can only view them so this is kind of the policy that you are defining you're going to instantiate that policy with data so we're going to provide open fgaa the data he needs to use to to evaluate the policy and we're going to do that in the form of what we call relationship tles that they have this form user object relationship and if you see the way it's the colors match right so organization Acme is the type so we're saying that the user Marie is related as a member to the specific organization right so a user ID and a an uh organization ID so we can in this case we're saying Marie is a member and an is an admin okay with this data that we have in tles we are actually going to
