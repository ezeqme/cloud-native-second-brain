---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["Security", "Storage Data"]
speakers: ["Yoshiyuki Tabata", "Hitachi", "Ltd.", "Gabriele Bartolini", "EDB"]
sched_url: https://kccncna2025.sched.com/event/27FXv/modern-postgresql-authorization-with-keycloak-cloud-native-identity-meets-database-security-yoshiyuki-tabata-hitachi-ltd-gabriele-bartolini-edb
youtube_search_url: https://www.youtube.com/results?search_query=Modern+PostgreSQL+Authorization+With+Keycloak%3A+Cloud+Native+Identity+Meets+Database+Security+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Modern PostgreSQL Authorization With Keycloak: Cloud Native Identity Meets Database Security - Yoshiyuki Tabata, Hitachi, Ltd. & Gabriele Bartolini, EDB

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Storage Data]]
- País/cidade: United States / Atlanta
- Speakers: Yoshiyuki Tabata, Hitachi, Ltd., Gabriele Bartolini, EDB
- Schedule: https://kccncna2025.sched.com/event/27FXv/modern-postgresql-authorization-with-keycloak-cloud-native-identity-meets-database-security-yoshiyuki-tabata-hitachi-ltd-gabriele-bartolini-edb
- Busca YouTube: https://www.youtube.com/results?search_query=Modern+PostgreSQL+Authorization+With+Keycloak%3A+Cloud+Native+Identity+Meets+Database+Security+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Modern PostgreSQL Authorization With Keycloak: Cloud Native Identity Meets Database Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXv/modern-postgresql-authorization-with-keycloak-cloud-native-identity-meets-database-security-yoshiyuki-tabata-hitachi-ltd-gabriele-bartolini-edb
- YouTube search: https://www.youtube.com/results?search_query=Modern+PostgreSQL+Authorization+With+Keycloak%3A+Cloud+Native+Identity+Meets+Database+Security+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TYgPemq06fg
- YouTube title: Modern PostgreSQL Authorization With Keycloak: Cloud Native... Yoshiyuki Tabata & Gabriele Bartolini
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/modern-postgresql-authorization-with-keycloak-cloud-native-identity-me/TYgPemq06fg.txt
- Transcript chars: 24331
- Keywords: authorization, posgus, access, database, client, device, authentication, policy, identity, native, connect, module, request, validator, security, feature, complete, session

### Resumo baseado na transcript

So, one of my favorite things about being a part of the CNCF is the opportunity for synergy between projects. So, this is a way we can collaborate with other projects to solve hard problems and innovate together. I always say that devops is the reason why I got into kubernetes and the reason why I will move away one day from it. uh cloud netpg is a popular open-source kubernetes operator for posgus uh originally developed by uh my company EDB and now it's a CNCF uh sandbox project and today we actually applied for the incubation u its job is to be a kind of a and we want to demonstrate how this shared community drives solid integration not just for features that we have today but for the powerful new features that we are developing uh together like the one that we are showing uh today. Keyclo uses the posgus database to store its data and if you're in kubernetes for example you can leverage cloud npg or any other operator or any other way to run posgus in in kubernetes but as I said before this is a status quo

### Excerpt da transcript

Good evening. So, one of my favorite things about being a part of the CNCF is the opportunity for synergy between projects. So, this is a way we can collaborate with other projects to solve hard problems and innovate together. So, welcome to our talk. We are here today with Yoshuki and myself to show you a brand new collaboration between two of these two of these CNCF projects. uh a collaboration that aims to fundamentally improve the way we authenticate and authorize access to posgus databases in cloud native environments. >> Okay. So hello everyone uh my name is Yoshik Tabata and I'm a senior consultant and I specialize in securing API and identity for enterprise and cloud native platforms with over 10 years of experience designing secure API ecosystems and identity solutions and as a tech lead for CSF security and compliance I contribute to best practices white papers and proposal reviews and facilitate region meetings I'm also an active open source contributor especially to Kikro as a language maintener and feature feature developer.

In addition, I organize community events such as Kro on Japan, speak at conference like Cubon and write books and articles on IM and Kro. Yeah. And I'm Gabriel Bolini. I'm VP and chief architect for Kubernetes. I've been using posgus for 25 years and uh I'm a possess contributor. I'm also a data and kubernetes ambassador where I I basically foster the adoption of uh stateful workloads in in kubernetes. Um I'm a devops evangelist. I always say that devops is the reason why I got into kubernetes and the reason why I will move away one day from it. and in the FOSGA space I'm also renowned for for a contribution in the backup and recovery space which is barman and lately in the uh for the clinp uh software of which I'm a CNCF maintainer. So this is the agenda for today. I will give you a brief introduction about clonerpg then yoshuki will talk about keylo and finally we will show how kiko and po posgugust integrate. So um so on the left as I said we've got Kiklo and Yoshiuki uh will we'll be talking about it.

Key is a CNCF incubating project and a complete open-source identity and access management solution. uh cloud netpg is a popular open-source kubernetes operator for posgus uh originally developed by uh my company EDB and now it's a CNCF uh sandbox project and today we actually applied for the incubation u its job is to be a kind of a robot DBA uh that handles the full life cycle management of a posgus cluster from insta
