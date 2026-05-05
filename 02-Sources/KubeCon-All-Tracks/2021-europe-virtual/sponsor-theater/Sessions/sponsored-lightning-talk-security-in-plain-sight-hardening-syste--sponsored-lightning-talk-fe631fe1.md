---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Sponsor Theater"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Phillip Gibson", "Microsoft Azure"]
sched_url: https://kccnceu2021.sched.com/event/igUZ/sponsored-lightning-talk-security-in-plain-sight-hardening-systems-via-open-source-phillip-gibson-microsoft-azure
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Security+In+Plain+Sight%3A+Hardening+Systems+Via+Open+Source+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Lightning Talk: Security In Plain Sight: Hardening Systems Via Open Source - Phillip Gibson, Microsoft Azure

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Sponsor Theater]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Phillip Gibson, Microsoft Azure
- Schedule: https://kccnceu2021.sched.com/event/igUZ/sponsored-lightning-talk-security-in-plain-sight-hardening-systems-via-open-source-phillip-gibson-microsoft-azure
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Security+In+Plain+Sight%3A+Hardening+Systems+Via+Open+Source+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Lightning Talk: Security In Plain Sight: Hardening Systems Via Open Source.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/igUZ/sponsored-lightning-talk-security-in-plain-sight-hardening-systems-via-open-source-phillip-gibson-microsoft-azure
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Security+In+Plain+Sight%3A+Hardening+Systems+Via+Open+Source+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OLmf1xLNICo
- YouTube title: Sponsored Lightning Talk: Security In Plain Sight: Hardening Systems Via Open Source- Phillip Gibson
- Match score: 0.996
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-lightning-talk-security-in-plain-sight-hardening-systems-via/OLmf1xLNICo.txt
- Transcript chars: 4347
- Keywords: source, cluster, security, outside, mesh, operational, projects, provides, application, compliance, tooling, simplify, enable, container, secrets, secret, moving, access

### Resumo baseado na transcript

hello everyone my name is phil gibson the program manager on the open source upstream team here at microsoft and today i want to talk to you about securing your open source adoption so as we know kubernetes has been a game changer for many organizations and with its rapid adoption transparency into compliance matters even more this intersection between cloud native architectures open source tooling and day zero operational governance has amplified the need to simplify ways to achieve compliance and controls so with azure we found it makes

### Excerpt da transcript

hello everyone my name is phil gibson the program manager on the open source upstream team here at microsoft and today i want to talk to you about securing your open source adoption so as we know kubernetes has been a game changer for many organizations and with its rapid adoption transparency into compliance matters even more this intersection between cloud native architectures open source tooling and day zero operational governance has amplified the need to simplify ways to achieve compliance and controls so with azure we found it makes sense to build our kubernetes ecosystem projects upstream first in open source we think open source tooling is the best way to enable highly ready kubernetes so today let's take a walk through some of these exciting projects in the security space built on top of the open policy agent project as a cross organization collaboration gatekeeper provides the ability to evaluate and validate configurations being deployed to a kubernetes cluster users can craft their policies using regular templates to meet their company's operational compliance requirements such as using only authorized container registries and container images to allow and disallow with ease safely store your kubernetes secrets outside of your cluster with the secret store csi project kubernetes secrets made it easy and convenient to store sensitive information outside of your application but this is still within the confines of your cluster the secret store csi project keeps all the look and feel of the kubernetes secret intact but adds additional protection moving your secrets outside the cluster for seamless experience the azure active directory pod managed identity project provides you with flexibility to control what access and application of kubernetes can have cluster operators can configure fine grained controls on authorizing pods to access resources outside the kubernetes cluster such as a such as access to a database without the need to have authentication logic inside your application use this open source project to simplify your cloud native application resources by moving the authorization logic out of the container and onto the kubernetes cluster service meshes simplify securing and routing traffic both inside and outside a kubernetes cluster moving service mesh configurations out of the applications to make it an operational configuration component service the service mesh interface specification project provides a common integration and configu
