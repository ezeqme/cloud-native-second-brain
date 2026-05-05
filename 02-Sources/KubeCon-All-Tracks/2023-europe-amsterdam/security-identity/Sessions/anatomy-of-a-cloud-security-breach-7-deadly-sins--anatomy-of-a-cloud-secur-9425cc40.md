---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security"]
speakers: ["Maya Levine", "Sysdig"]
sched_url: https://kccnceu2023.sched.com/event/1HyYf/anatomy-of-a-cloud-security-breach-7-deadly-sins-maya-levine-sysdig
youtube_search_url: https://www.youtube.com/results?search_query=Anatomy+of+a+Cloud+Security+Breach+-+7+Deadly+Sins+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Anatomy of a Cloud Security Breach - 7 Deadly Sins - Maya Levine, Sysdig

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Maya Levine, Sysdig
- Schedule: https://kccnceu2023.sched.com/event/1HyYf/anatomy-of-a-cloud-security-breach-7-deadly-sins-maya-levine-sysdig
- Busca YouTube: https://www.youtube.com/results?search_query=Anatomy+of+a+Cloud+Security+Breach+-+7+Deadly+Sins+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Anatomy of a Cloud Security Breach - 7 Deadly Sins.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYf/anatomy-of-a-cloud-security-breach-7-deadly-sins-maya-levine-sysdig
- YouTube search: https://www.youtube.com/results?search_query=Anatomy+of+a+Cloud+Security+Breach+-+7+Deadly+Sins+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xc5uvkHtFrA
- YouTube title: Anatomy of a Cloud Security Breach - 7 Deadly Sins - Maya Levine, Sysdig
- Match score: 0.915
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/anatomy-of-a-cloud-security-breach-7-deadly-sins/xc5uvkHtFrA.txt
- Transcript chars: 27829
- Keywords: attackers, mining, attack, crypto, access, container, actually, attacks, credentials, attacker, malicious, github, breach, security, threat, server, control, images

### Resumo baseado na transcript

hello everybody my name is Maya LaVine I'm a product manager here at cig and today I'm going to talk to you about real Cloud security breaches that have occurred and how you can prevent them from happening to you basically and I want to do a quick disclaimer if your company is one of the ones that are mentioned here I apologize in advance for the ptsc that I'm probably bringing on but in all seriousness I do feel that as an industry we should should be as open

### Excerpt da transcript

hello everybody my name is Maya LaVine I'm a product manager here at cig and today I'm going to talk to you about real Cloud security breaches that have occurred and how you can prevent them from happening to you basically and I want to do a quick disclaimer if your company is one of the ones that are mentioned here I apologize in advance for the ptsc that I'm probably bringing on but in all seriousness I do feel that as an industry we should should be as open as possible about why and how breaches have occurred I never shame anybody for being the victim of a breach especially because they're only becoming more and more common in fact a Verizon 2021 report showed that cloud assets are actually starting to become more targeted than on premise assets for breaches and if we think about some of the more major attacks in the cloud versus on premise let's start with ransomware on premise it's usually a fishing email but in the cloud It's All About Storage databases and there's many different paths that attackers can take to get there could be misconfigurations or overly permissive policies and when we think of supply chain compromises it's arguably a lot easier to execute those in the cloud because of the modern way that applications are being built with many services and it's just harder to tell kind of what is using what and finally crypto mining cloud is probably the perfect breeding ground for crypto mining attacks due to the infinite amount of elastic compute that most users have access to so jumping right in to our first attack the focus on this one is ransomware and unlike in Austin Powers it's never really a laughing matter in this case the victim was onus which is one of the biggest cryptocurrency Platforms in Vietnam and attackers were able to exploit a log for J vulnerability in a cyclo server of onus and they left back doors behind and named them kworker for the purpose of disguising as the Linux operating systems kworker service and that was used as a tunnel to connect back to their command and control server via SSH which is a wise way to avoid detection so the attackers established a remote shell and discovered a a configuration file which held AWS credentials now these credentials had full access permissions so using them the attackers were able to access S3 buckets and continue with an extortion scheme the next day onus discovered that customer data had been deleted from their S3 buckets and so of course at this point they deactivated all of the
