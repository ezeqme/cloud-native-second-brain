---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Brad Micklea", "Jozu", "Gavrish Prabhu", "Nutanix"]
sched_url: https://kccnceu2026.sched.com/event/2CVyT/your-models-are-vulnerable-how-kitops-turns-kserve-into-a-zero-trust-inference-platform-brad-micklea-jozu-gavrish-prabhu-nutanix
youtube_search_url: https://www.youtube.com/results?search_query=Your+Models+Are+Vulnerable%3A+How+KitOps+Turns+KServe+Into+a+Zero-Trust+Inference+Platform+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Your Models Are Vulnerable: How KitOps Turns KServe Into a Zero-Trust Inference Platform - Brad Micklea, Jozu & Gavrish Prabhu, Nutanix

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Brad Micklea, Jozu, Gavrish Prabhu, Nutanix
- Schedule: https://kccnceu2026.sched.com/event/2CVyT/your-models-are-vulnerable-how-kitops-turns-kserve-into-a-zero-trust-inference-platform-brad-micklea-jozu-gavrish-prabhu-nutanix
- Busca YouTube: https://www.youtube.com/results?search_query=Your+Models+Are+Vulnerable%3A+How+KitOps+Turns+KServe+Into+a+Zero-Trust+Inference+Platform+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Your Models Are Vulnerable: How KitOps Turns KServe Into a Zero-Trust Inference Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyT/your-models-are-vulnerable-how-kitops-turns-kserve-into-a-zero-trust-inference-platform-brad-micklea-jozu-gavrish-prabhu-nutanix
- YouTube search: https://www.youtube.com/results?search_query=Your+Models+Are+Vulnerable%3A+How+KitOps+Turns+KServe+Into+a+Zero-Trust+Inference+Platform+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OE6t8_V7ZU4
- YouTube title: Your Models Are Vulnerable: How KitOps Turns KServe Into a Zero-Tru... Brad Micklea & Gavrish Prabhu
- Match score: 0.853
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/your-models-are-vulnerable-how-kitops-turns-kserve-into-a-zero-trust-i/OE6t8_V7ZU4.txt
- Transcript chars: 35735
- Keywords: actually, registry, container, security, models, deploy, inference, training, verification, whatever, production, already, storage, talking, create, compliance, wanted, kitops

### Resumo baseado na transcript

We're going to jump in and talk about why your AI is vulnerable and how to make it less vulnerable. I am a maintainer of both the model pack specification and the kitops project inside CNCF. all's good so that's about Kserve >> all right so Kerve as Gish mentioned makes serving very easy but you're the ones that are responsible for adding security. Um, but depending on the security posture of your organization, you may want to instead have them that require failed open obviously. That's going to create an operational pause if there's a problem, but it's not going to create a security issue. You get the benefits of content addressable storage which when you're talking about gigabytes and tens of gigabytes and hundreds of gigabytes payloads that content addressable storage can be a huge gain over something like just throwing stuff in S3.

### Excerpt da transcript

Welcome. Thank you uh for spending a few minutes with us. We're going to jump in and talk about why your AI is vulnerable and how to make it less vulnerable. My name is uh Brad Mikley. I am a maintainer of both the model pack specification and the kitops project inside CNCF. Uh I'm also the CEO of Jozu, which is a commercial company that uses the kitops and model pack technology. Uh hi, I'm Gavish Prabhu. Uh I work at Nutanix. I was one of the founding engineers at Nutanix Enterprise AI. So I'm also a maintainer in case and also now a maintainer in on my AI gateway. >> All right. Do you want to talk about KERF? >> Yes. So Keser has been around for some time. It was a sub project under CubeFlow. Then it took its own direction. So the main purpose of this project is to help you deploy your inference workloads with any runtime in just like few clicks. We have something called as a inference service which is our custom CD sorry CD and we use that extensively for all our uh selective runtimes. You can choose VLM, you can choose SG lang, you can bring the traditional ML models, anything.

And this is a complete box with both generative AI and predictive AI. So it's very simple just one CR and you're good to go. We also have very good integrations with LMD. There are a lot of talks with LMD. It's the new hot topic this year and we have something called as LLM infant service. It's a new CR. We saw that there is very much need a different like a good integration with all the things LLMD needs. It can be KV cache, it can be like GI integration, any gateway you want to bring all those things will come in. And now also disagregated inference you want a different PD part good we'll give you all in the LM inference service C and all along with this KSER has also its own uh in-house autoscaling it will help you with all your networking everything so all's good so that's about Kserve >> all right so Kerve as Gish mentioned makes serving very easy but you're the ones that are responsible for adding security. Um, it is not designed to be an exceptionally secure. It's meant to be exceptionally easy.

Um, so you're going to need to verify that the model or agent that is being served, MCT server, whatever it is, is the same one that was approved. Um, you want to make sure to validate signatures. You want to make sure to validate addations before you go and load weights. You want to track the data set that was used for training or was used for validation. You want to make sure
