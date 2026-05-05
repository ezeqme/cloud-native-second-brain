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
themes: ["AI ML", "Community Governance"]
speakers: ["Alexander Schwartz", "Red Hat", "Yuuichi Nakamura", "Hitachi"]
sched_url: https://kccnceu2023.sched.com/event/1LQDS/keycloak-the-open-source-iam-for-modern-applications-alexander-schwartz-red-hat-yuuichi-nakamura-hitachi
youtube_search_url: https://www.youtube.com/results?search_query=Keycloak%3A+The+Open-Source+IAM+for+Modern+Applications+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Keycloak: The Open-Source IAM for Modern Applications - Alexander Schwartz, Red Hat & Yuuichi Nakamura, Hitachi

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alexander Schwartz, Red Hat, Yuuichi Nakamura, Hitachi
- Schedule: https://kccnceu2023.sched.com/event/1LQDS/keycloak-the-open-source-iam-for-modern-applications-alexander-schwartz-red-hat-yuuichi-nakamura-hitachi
- Busca YouTube: https://www.youtube.com/results?search_query=Keycloak%3A+The+Open-Source+IAM+for+Modern+Applications+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Keycloak: The Open-Source IAM for Modern Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1LQDS/keycloak-the-open-source-iam-for-modern-applications-alexander-schwartz-red-hat-yuuichi-nakamura-hitachi
- YouTube search: https://www.youtube.com/results?search_query=Keycloak%3A+The+Open-Source+IAM+for+Modern+Applications+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=j7FwsYJCocA
- YouTube title: Keycloak: The Open-Source IAM for Modern Applications - Alexander Schwartz & Yuuichi Nakamura
- Match score: 0.823
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/keycloak-the-open-source-iam-for-modern-applications/j7FwsYJCocA.txt
- Transcript chars: 29599
- Keywords: security, client, grafana, access, password, metrics, profiles, operator, support, database, around, source, configure, documentation, connect, screen, enabled, realms

### Resumo baseado na transcript

key cloak the open source identity and access management for modern application welcome to this talk here at kubecon we're very happy to be in our cncf project uh we that's giglog and today I have UVC Nakamura here from Hitachi and I'm Alexander from Red Hat I'm here I'm working at redhead for a year now but I looked it up so I did my first pull request that was accepted on key cloak I think in 2015 or so and then like last year following redhead full time

### Excerpt da transcript

key cloak the open source identity and access management for modern application welcome to this talk here at kubecon we're very happy to be in our cncf project uh we that's giglog and today I have UVC Nakamura here from Hitachi and I'm Alexander from Red Hat I'm here I'm working at redhead for a year now but I looked it up so I did my first pull request that was accepted on key cloak I think in 2015 or so and then like last year following redhead full time uh working on the Key Club project so yeah Key Club was it it's an open source identity and access management solution and the great thing about open source is that you can tweak it the way you like it you can use it for authentication authorizing users in your applications you can configure it interactively or fully automated so I'm a big fan of full automation you convert it to existing security infrastructures so um in a normal I would say Enterprise environment you usually have maybe an existing ldub maybe existing Legacy user database and you can connect those you can also extend and customize it as needed as I said it's open source but we also offer lots of service provider interfaces as we call them where you can write your own modules load them into key cloak and do the things that you need to do and it runs and scales both in the cloud and non-cloud environments and yeah that's it that's key clock and it I would say a very whole and good package to manage all your users and your way about inclined so what does key Glock do um well it all starts with the user here they have their mobile devices they have their laptops they have their apps and they want to access some services in the cloud so and once they do that without an access token at first they will be redirected to keycloud keyclock will present a logging screen and once they enter their username and password or their other methods of Authentication they will then receive a token and then they try again with token accessing that service and the service can use that token to verify that it's really valid and find out about uh what the user is then uh maybe has some rows what they're allow to do uh what's their username what's their password about the username and the email address all that can be done retrieved using that token and it's all about not handing the password or credentials to the application themselves okay so um and in a I would say in a key you can run keyclock with its own database so click log make sure that all the user pa
