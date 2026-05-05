---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security", "SRE Reliability"]
speakers: ["Maya Levine", "Sysdig"]
sched_url: https://kccnceu2024.sched.com/event/1YeQb/iam-confused-analyzing-8-identity-breach-incidents-maya-levine-sysdig
youtube_search_url: https://www.youtube.com/results?search_query=IAM+Confused%3A+Analyzing+8+Identity+Breach+Incidents+CNCF+KubeCon+2024
slides: []
status: parsed
---

# IAM Confused: Analyzing 8 Identity Breach Incidents - Maya Levine, Sysdig

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Maya Levine, Sysdig
- Schedule: https://kccnceu2024.sched.com/event/1YeQb/iam-confused-analyzing-8-identity-breach-incidents-maya-levine-sysdig
- Busca YouTube: https://www.youtube.com/results?search_query=IAM+Confused%3A+Analyzing+8+Identity+Breach+Incidents+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre IAM Confused: Analyzing 8 Identity Breach Incidents.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQb/iam-confused-analyzing-8-identity-breach-incidents-maya-levine-sysdig
- YouTube search: https://www.youtube.com/results?search_query=IAM+Confused%3A+Analyzing+8+Identity+Breach+Incidents+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=B0Xm2kfU-yA
- YouTube title: IAM Confused: Analyzing 8 Identity Breach Incidents - Maya Levine, Sysdig
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/iam-confused-analyzing-8-identity-breach-incidents/B0Xm2kfU-yA.txt
- Transcript chars: 28895
- Keywords: credentials, access, attack, attackers, actually, identity, security, permissions, attacker, looking, management, threat, privileges, cluster, important, resources, called, secrets

### Resumo baseado na transcript

thank you for coming on a Friday afternoon no less my name is Maya LaVine and today's talk is going to be about identity security the name is I am confused and so I have a question for you all when it comes to Identity are you confused if you are it completely makes sense because things are so complicated and evolving so quickly identity in the cloud is a relatively new frontier but it is a essential and non-negotiable to be investing in it and getting it right identity

### Excerpt da transcript

thank you for coming on a Friday afternoon no less my name is Maya LaVine and today's talk is going to be about identity security the name is I am confused and so I have a question for you all when it comes to Identity are you confused if you are it completely makes sense because things are so complicated and evolving so quickly identity in the cloud is a relatively new frontier but it is a essential and non-negotiable to be investing in it and getting it right identity is like the perimeter of the cloud and almost every cloud breach that we've seen in the past few years has taken advantage of mismanaged permissions secrets and identities as an industry we are struggling when it comes to identity management especially when it comes to how many permissions we're granting versus actually using statistic threat research found that 98% of permissions that are granted are actually unused and that's a huge scope for an attacker to take advantage of especially considering a lot of us are utilizing default roles which generally have a lot of permissions granting to them versus creating our own custom specific roles and there's quite a few challenges with identity security including the fact that ownership of identity posture between Dev Ops and security is often unclear and this can lead to mistakes that stem from going too fast in addition human and machine identity management is not easy I really like the metaphor of a key under the mat if I'm a robber and I'm scoping out your house and I notice you're gone on vacation the first place I'm going to look is somewhere like under the mat where I know people tend to leave their keys similarly attackers are very good at secret harvesting and they know where to look and this is everywhere from serverless function code IAC software things like terraform State files they often contain credentials and secrets and otherwise sensitive information that gets overlooked because they're kind of obscure in addition SAS applications are a huge attack surface credentials are being left everywhere from repos to GitHub to ad to slack and developers can underestimate the power of readon access that's all attackers need in order to read a secret the point here is that attackers are actually better than we are at Secrets management because for them getting a credential with great access is their golden ticket it's what will enable them to escalate their Privileges and escalate their attacks while while for Defenders this is usually not
