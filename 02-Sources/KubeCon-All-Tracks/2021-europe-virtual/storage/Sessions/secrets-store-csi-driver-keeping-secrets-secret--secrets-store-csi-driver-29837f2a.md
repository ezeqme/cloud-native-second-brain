---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Storage"
themes: ["Storage Data"]
speakers: ["Anish Ramasekar", "Microsoft", "Tommy Murphy", "Google"]
sched_url: https://kccnceu2021.sched.com/event/iE3L/secrets-store-csi-driver-keeping-secrets-secret-anish-ramasekar-microsoft-tommy-murphy-google
youtube_search_url: https://www.youtube.com/results?search_query=Secrets+Store+CSI+Driver%3A+Keeping+Secrets+Secret+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Secrets Store CSI Driver: Keeping Secrets Secret - Anish Ramasekar, Microsoft & Tommy Murphy, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Storage]]
- Temas: [[Storage Data]]
- País/cidade: Virtual / Virtual
- Speakers: Anish Ramasekar, Microsoft, Tommy Murphy, Google
- Schedule: https://kccnceu2021.sched.com/event/iE3L/secrets-store-csi-driver-keeping-secrets-secret-anish-ramasekar-microsoft-tommy-murphy-google
- Busca YouTube: https://www.youtube.com/results?search_query=Secrets+Store+CSI+Driver%3A+Keeping+Secrets+Secret+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Secrets Store CSI Driver: Keeping Secrets Secret.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3L/secrets-store-csi-driver-keeping-secrets-secret-anish-ramasekar-microsoft-tommy-murphy-google
- YouTube search: https://www.youtube.com/results?search_query=Secrets+Store+CSI+Driver%3A+Keeping+Secrets+Secret+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KOh43en5dEY
- YouTube title: Secrets Store CSI Driver: Bringing external secrets in house
- Match score: 0.816
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/secrets-store-csi-driver-keeping-secrets-secret/KOh43en5dEY.txt
- Transcript chars: 23438
- Keywords: secret, driver, provider, secrets, external, volume, keyword, rotation, running, namespace, certificate, feature, application, providers, required, resource, deploy, controller

### Resumo baseado na transcript

hey everyone welcome to cncf on demand webinar today i'm going to talk about the secret store csi driver that integrates external secret stores with kubernetes a brief introduction about me i'm anish i'm a software engineer at microsoft based in seattle i'm part of the upstream kubernetes security team [Music] i am a maintainer of the secret store csi driver and the azure keyword provider for the secret store csi driver so why are we talking about external secret storage when kubernetes has a perfectly good one built in

### Excerpt da transcript

hey everyone welcome to cncf on demand webinar today i'm going to talk about the secret store csi driver that integrates external secret stores with kubernetes a brief introduction about me i'm anish i'm a software engineer at microsoft based in seattle i'm part of the upstream kubernetes security team [Music] i am a maintainer of the secret store csi driver and the azure keyword provider for the secret store csi driver so why are we talking about external secret storage when kubernetes has a perfectly good one built in first kubernetes secrets may not meet your data addressed encryption requirements by default when you create a kubernetes secret the data is stored in xcd and it's just basics before encoded but it's not encrypted although there are kms providers to enable secret data encryption at rest depending on your organization you may have already standardized on a third party secret solution and need to use that also your external secret solution may have some sort of secret rotation story or integration that you are looking to leverage finally if your organization has already invested in auditing and alerting on a third-party secret system you may want to you may not want to duplicate that effort for community secret so what do you do there are a few options to consume external secrets you first might look at modifying your application to fetch the secret from external api directly using the sdks provided by the external sql store providers this may not be possible depending on your deployment you may not have the code to edit or it may be prohibitively expensive to implement these changes and if you're targeting deployments against multiple secret providers this effort would need to be duplicated across every single secret storage system uh you might also look at just copying the secrets and syncing them as kubernetes secrets perhaps with a single controller this is portable and won't require application changes but you may lose out on some of the benefits of your external secret stores like using the identity of the workload for access controls because in this particular scenario you are granting the single controller permissions to access the secrets instead of the workload that needs to use the secret the third option is you could use a sidecar to fetch and write these secrets the sidecar may be injected using a mutating web hook here the identity that is being used to access the external secret store would still be the pod identity but having
