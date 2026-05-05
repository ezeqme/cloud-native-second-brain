---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Alexander Schwartz", "Red Hat", "Takashi Norimatsu", "Hitachi", "Ltd."]
sched_url: https://kccncna2023.sched.com/event/1R2mH/10-years-of-keycloak-whats-next-for-cloud-native-authentication-and-oidc-alexander-schwartz-red-hat-takashi-norimatsu-hitachi-ltd
youtube_search_url: https://www.youtube.com/results?search_query=10+Years+of+Keycloak+-+What%27s+Next+for+Cloud-Native+Authentication+and+OIDC%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# 10 Years of Keycloak - What's Next for Cloud-Native Authentication and OIDC? - Alexander Schwartz, Red Hat & Takashi Norimatsu, Hitachi, Ltd.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Alexander Schwartz, Red Hat, Takashi Norimatsu, Hitachi, Ltd.
- Schedule: https://kccncna2023.sched.com/event/1R2mH/10-years-of-keycloak-whats-next-for-cloud-native-authentication-and-oidc-alexander-schwartz-red-hat-takashi-norimatsu-hitachi-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=10+Years+of+Keycloak+-+What%27s+Next+for+Cloud-Native+Authentication+and+OIDC%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre 10 Years of Keycloak - What's Next for Cloud-Native Authentication and OIDC?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2mH/10-years-of-keycloak-whats-next-for-cloud-native-authentication-and-oidc-alexander-schwartz-red-hat-takashi-norimatsu-hitachi-ltd
- YouTube search: https://www.youtube.com/results?search_query=10+Years+of+Keycloak+-+What%27s+Next+for+Cloud-Native+Authentication+and+OIDC%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SuGkRJVrod0
- YouTube title: 10 Years of Keycloak - What's Next for Cloud-Native Authen... Alexander Schwartz & Takashi Norimatsu
- Match score: 0.836
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/10-years-of-keycloak-whats-next-for-cloud-native-authentication-and-oi/SuGkRJVrod0.txt
- Transcript chars: 25144
- Keywords: security, keycloak, profiles, profile, working, command, identity, access, connect, support, supporting, activity, client, started, version, questions, called, therefore

### Resumo baseado na transcript

so the usual questions I ask at Cube conert at the very beginning who's been using kloo for I don't know more than three years in production maybe hands up all right that's cool um who is using it for a year in production all right who's been trying it out locally on the desktop who's hearing about klock for the very first time today all right cool right so um we will be jumping right into the middle um still giving some introduction where KY is coming from but key clo to connect to kubernetes and to make it all work with with checking these tokens that are then passed back and forth right so kickl as I said Is An Open Source identity and access management solution we have lots of authentication standard

### Excerpt da transcript

so the usual questions I ask at Cube conert at the very beginning who's been using kloo for I don't know more than three years in production maybe hands up all right that's cool um who is using it for a year in production all right who's been trying it out locally on the desktop who's hearing about klock for the very first time today all right cool right so um we will be jumping right into the middle um still giving some introduction where KY is coming from but um maybe you want to look at the uh Amsterdam presentation for a more in-depth early startup guide on on KY clo right so video crew are we ready yet or not yet yet we're ready okay thumb up that's good so welcome um welcome to the talk 10 years of keycloak what's next for cloud native authentication and oidc um together with me is here tekashi norimatsu Pachi uh my name is Alexander FS from redhead we are both maintainers on the keylog project and guides you through the next 35 minutes and we will also do a Q&A then at the end which will be part of the 35 minutes right so let's give it a go um keycloak well what is keycloak it's an open source identity and access management solution so basically it presents a login screen to users and the initial commit I would say the birth date of that piece of software was then uh in July 2013 and that's almost 10 years ago so that's why we named this talk 10 years of KL um KL at the very beginning well it was always presenting a login screen to the user putting in username and password um and what do you need to do that uh you need to have an open ID connect protocol implementation on the server um because that was new and hot stuff at the time and you need to have some Services some database some apis to store information about your applications which are then kind of called clients and identities which are then called users right and and from the very beginning it was from Developers for developers so you could always extend keycloak it has apis it has um yeah service provider interfaces as we call them you can do some Java programming and do the things that you need to do in your environment with kloog and that's was in there from the very beginning and we kept that over all the time soon after that we added more functionality it was multiactor authentication um client libraries um so for all the for lots of Frameworks during the time there were then implementations of keylo clients libraries and we added things like saml Elder up all the things that you need
