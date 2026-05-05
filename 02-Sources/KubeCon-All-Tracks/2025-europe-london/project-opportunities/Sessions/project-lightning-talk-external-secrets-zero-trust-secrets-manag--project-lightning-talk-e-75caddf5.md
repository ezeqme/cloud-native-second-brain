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
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Moritz Johner", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcv5/project-lightning-talk-external-secrets-zero-trust-secrets-management-with-eso-moritz-johner-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+external-secrets%3A+Zero+Trust+Secrets+Management+with+ESO+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: external-secrets: Zero Trust Secrets Management with ESO - Moritz Johner, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Moritz Johner, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcv5/project-lightning-talk-external-secrets-zero-trust-secrets-management-with-eso-moritz-johner-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+external-secrets%3A+Zero+Trust+Secrets+Management+with+ESO+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: external-secrets: Zero Trust Secrets Management with ESO.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcv5/project-lightning-talk-external-secrets-zero-trust-secrets-management-with-eso-moritz-johner-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+external-secrets%3A+Zero+Trust+Secrets+Management+with+ESO+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9mX9PvNNDjk
- YouTube title: Project Lightning Talk: external-secrets: Zero Trust Secrets Management with ESO - Moritz Johner
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-external-secrets-zero-trust-secrets-management/9mX9PvNNDjk.txt
- Transcript chars: 4630
- Keywords: secrets, secret, manager, external, management, operator, cluster, static, authenticate, workload, resource, provider, providers, represents, having, everything, password, quickly

### Resumo baseado na transcript

I am one of the maintainers and original creators of external secrets operator. Um yeah I want to quickly share what we've been done in the past couple of years I guess and give you a quick overview of how it works and how you can use it to do zero trust uh secrets management with ESO. Um we can decode that as well and can see okay the password is there mingle mingle um and with that um that's it from the demo. You can reach out on us on Slack in the Kubernetes Slack in the external secrets um uh channel.

### Excerpt da transcript

Hello everyone and welcome to the session. My name is Morris Joner. I am one of the maintainers and original creators of external secrets operator. Um yeah I want to quickly share what we've been done in the past couple of years I guess and give you a quick overview of how it works and how you can use it to do zero trust uh secrets management with ESO. So ESO is built around the assumption that an engineering team stores all of their secrets within one secure vault. That's like the underlying assumption. Um now ESO runs as a workload inside your cluster um and it reaches out to that vault and um fetches secrets from there and with that data it creates a Kubernetes secret object and from there people can use it. By people I mean like workloads. You can uh reference it from an ingress resource. You can um mount it as a file in a pot or consume it as a environment variable. Now one thing that you should not do is use static secrets or stack static credentials to reach out to that vault. Um instead you want to leverage something um of the underlying platform to authenticate with that provider.

We've built that um and we're simply just using um Kubernetes uh service accounts and we throw them against that vault uh to authenticate. That's something that I guess like most of the providers um support today. Um by providers I mean that could be Adable Secrets Manager, GCP secret manager, Azure Key Vault, Hashi Corp Vault and like all of the other secret vaults that are out there. Uh as of today we support about like 30ish providers. So I guess most of most of us uh should be covered. Um yeah and so the operator runs as a workload in your cluster and then you can have a secret store resource that represents the provider and how to authenticate with that provider and there's another resource external secret that represents the secret that is supposed to be created. Um, and because it's an operator and controller that runs, it does this on a regular basis, once an hour, every 10 minutes, every minute to just reconcile the state from the vault inside the cluster. Pretty simple. Um, we have a bunch of more features built in the past um, years, I guess.

Uh, zero trust, we already like talked about that. Um, on top of that, we have like secret rotation, so you can like securely rotate the secrets by having like different versions of secrets and um, throw them at your um, at your workload. So they can just handle it and maybe try try try both versions. There are like mul
