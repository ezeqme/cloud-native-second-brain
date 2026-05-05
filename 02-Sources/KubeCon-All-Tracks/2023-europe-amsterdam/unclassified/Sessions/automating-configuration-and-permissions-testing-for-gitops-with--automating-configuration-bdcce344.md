---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["GitOps Delivery"]
speakers: ["Eve Ben Ezra", "Michael Hume", "The New York Times"]
sched_url: https://kccnceu2023.sched.com/event/1HydS/automating-configuration-and-permissions-testing-for-gitops-with-opa-conftest-eve-ben-ezra-michael-hume-the-new-york-times
youtube_search_url: https://www.youtube.com/results?search_query=Automating+Configuration+and+Permissions+Testing+for+GitOps+with+OPA+Conftest+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Automating Configuration and Permissions Testing for GitOps with OPA Conftest - Eve Ben Ezra & Michael Hume, The New York Times

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Eve Ben Ezra, Michael Hume, The New York Times
- Schedule: https://kccnceu2023.sched.com/event/1HydS/automating-configuration-and-permissions-testing-for-gitops-with-opa-conftest-eve-ben-ezra-michael-hume-the-new-york-times
- Busca YouTube: https://www.youtube.com/results?search_query=Automating+Configuration+and+Permissions+Testing+for+GitOps+with+OPA+Conftest+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Automating Configuration and Permissions Testing for GitOps with OPA Conftest.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HydS/automating-configuration-and-permissions-testing-for-gitops-with-opa-conftest-eve-ben-ezra-michael-hume-the-new-york-times
- YouTube search: https://www.youtube.com/results?search_query=Automating+Configuration+and+Permissions+Testing+for+GitOps+with+OPA+Conftest+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VCX4UALQjeg
- YouTube title: Automating Configuration and Permissions Testing for GitOps with OPA...- Eve Ben Ezra & Michael Hume
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/automating-configuration-and-permissions-testing-for-gitops-with-opa-c/VCX4UALQjeg.txt
- Transcript chars: 29892
- Keywords: policy, policies, feedback, write, developers, latest, deployment, developer, infrastructure, configuration, application, shared, allowed, little, manifest, cubeconform, manifests, validation

### Resumo baseado na transcript

about the internal developer platform at the New York Times from there we'll dive into feedback and how it impacts developer productivity before going through an open comp test demo we'll talk about how we've implemented comp tests at the New York Times and how this has allowed us to take a trust but verify approach to application deployment including moving toward automatic merging of automatically generated files finally we'll take a peek into what we're doing next with schema validation using cubeconform so I want to start with some

### Excerpt da transcript

about the internal developer platform at the New York Times from there we'll dive into feedback and how it impacts developer productivity before going through an open comp test demo we'll talk about how we've implemented comp tests at the New York Times and how this has allowed us to take a trust but verify approach to application deployment including moving toward automatic merging of automatically generated files finally we'll take a peek into what we're doing next with schema validation using cubeconform so I want to start with some background and definitions just to make sure we're all on the same page and the first of those is get Ops get Ops is an operational framework that uses that utilizes git as a single source of Truth this is to manage infrastructure and application deployments and prevent configuration drift which occurs when the actual state of an application's infrastructure gradually diverges from its declarative state the next term is Argo CD a declarative continuous delivery tool that utilizes git Ops principles to simplify application deployment to a kubernetes cluster the next term I want to talk about is policy which refers to a set of rules that govern how a system operates in a specific scenario an example of a policy might be prohibiting the use of latest tags on container images or restricting a kubernetes container's ability to run as root and lastly I want to give you some background on Opa the open policy agent this is an open source general purpose policy engine that unifies policy enforcement across the cloud native stack our talk today pertains to a utility from Oppa which is conf test that allows you to write policy tests against structured configuration data this in turn allows you to offer fast feedback by enabling policy enforcement locally or in the CI process without ever needing to connect to a kubernetes cluster now I want to tell you a little bit more about the internal developer platform at the New York Times why we needed it what our mindset was with respect to governance and how the platform has improved developer productivity so as technology changes and evolves application developers need to learn more tools to keep up application developers spend less time developing features as they also integrate and manage containerization infrastructure as code testing building monitoring and more and seeing as these Technologies can be broken down even further you can understand that this quickly piles up and even if it we
