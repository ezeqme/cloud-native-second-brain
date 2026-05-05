---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security", "SRE Reliability"]
speakers: ["Yoshiyuki Tabata", "Hitachi", "Ltd."]
sched_url: https://kccncna2023.sched.com/event/1R2ma/challenge-to-implementing-scalable-authorization-with-keycloak-yoshiyuki-tabata-hitachi-ltd
youtube_search_url: https://www.youtube.com/results?search_query=Challenge+to+Implementing+%E2%80%9CScalable%E2%80%9D+Authorization+with+Keycloak+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Challenge to Implementing “Scalable” Authorization with Keycloak - Yoshiyuki Tabata, Hitachi, Ltd.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Yoshiyuki Tabata, Hitachi, Ltd.
- Schedule: https://kccncna2023.sched.com/event/1R2ma/challenge-to-implementing-scalable-authorization-with-keycloak-yoshiyuki-tabata-hitachi-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=Challenge+to+Implementing+%E2%80%9CScalable%E2%80%9D+Authorization+with+Keycloak+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Challenge to Implementing “Scalable” Authorization with Keycloak.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ma/challenge-to-implementing-scalable-authorization-with-keycloak-yoshiyuki-tabata-hitachi-ltd
- YouTube search: https://www.youtube.com/results?search_query=Challenge+to+Implementing+%E2%80%9CScalable%E2%80%9D+Authorization+with+Keycloak+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-m8FUNX1DP0
- YouTube title: Challenge to Implementing “Scalable” Authorization with Keycloak - Yoshiyuki Tabata, Hitachi, Ltd.
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/challenge-to-implementing-scalable-authorization-with-keycloak/-m8FUNX1DP0.txt
- Transcript chars: 19103
- Keywords: authorization, access, resource, policy, centralized, resources, scalable, regarding, availability, introduce, authentication, application, performance, decision, request, management, security, number

### Resumo baseado na transcript

here using key I explain how to make the logic calization scalable and how to make the architecture scalable and ensure availability I hope that this session will help developers Implement allation first of all please let me introduce myself my name is yoshu Tabata and I'm a senior OS senior OSS consultant at Hitachi and I have be become a sensive Ambassador in this form I mainly work as a specialist in API authorization for example I consult for API management infrastructure and authentication and authorization systems in the

### Excerpt da transcript

here using key I explain how to make the logic calization scalable and how to make the architecture scalable and ensure availability I hope that this session will help developers Implement allation first of all please let me introduce myself my name is yoshu Tabata and I'm a senior OS senior OSS consultant at Hitachi and I have be become a sensive Ambassador in this form I mainly work as a specialist in API authorization for example I consult for API management infrastructure and authentication and authorization systems in the financial public social and Industrial fields and I'm also contributor toess related to authentication authorization and API management for example I contribute to Kyro and ID and access management OSS and S scare and API management OSS for these OSS I mainly develop features based on feedback from actual projects like the above fields and other activities I spoke at events such as API days API specifications conference or security workshop and so on and I wrot some books and web articles about identity and access management so let's get started Le of today's contents first I describe the importance of authorization then I describe what scalable authorization is after that I introduce how to implement scalable authorization with KY clock then finally I introduce Advanced challenges with is Opa and cjb first I describe the importance of alization first what is authorization authorization is a process of verifying that a requested action or service is approved for a specific entity the important point is alization is different from authentication authentication is the process of verifying an entity's identity and authenticated doesn't mean authorized to access all resources for example a general user should not be authorized to access administrator features even if they are are authenticated and authentication is not always required for Access accessing resources for example there are public resources that can be accessed without Authentication in this way it is important to clearly distinguish between authentication and authorization today I will dive into authorization authorization is becoming more and more important to security considerations for example in or's top 10 AP security risks three of the top five security risks include the world authorization number one broken object authorization number three broken object property level authorization and number five broken functional level authorization I briefly explain each security
