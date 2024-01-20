import * as dotenv from 'dotenv';
import config from '../../config.json';

const webConfigJSON = {
  domainName: config.domain_name,
  backendSubdomain: config.backend_subdomain,
  backendDevSubdomain: config.backend_dev_subdomain,
  frontendDevSubdomain: config.frontend_dev_subdomain,
};

export const pipelineConfig = (env: string) => {
  if (env === 'Production') {
    const { parsed } = dotenv.config({ path: '.env.production' });

    return {
      buildCommand: 'npm run build:prod',
      deployCommand: 'npm run cdk deploy',
      branch: 'main',
      tag: 'infrastructure-production-pipeline',
      githubToken: parsed?.GITHUB_TOKEN,
      workspaceId: parsed?.WORKSPACE_ID,
      channelId: parsed?.CHANNEL_ID,
      ...webConfigJSON,
    };
  }

  const { parsed } = dotenv.config({ path: '.env.development' });

  return {
    buildCommand: 'npm run build:dev',
    deployCommand: 'npm run cdk:dev deploy',
    branch: 'dev',
    tag: 'infrastructure-development-pipeline',
    githubToken: parsed?.GITHUB_TOKEN,
    workspaceId: parsed?.WORKSPACE_ID,
    channelId: parsed?.CHANNEL_ID,
    ...webConfigJSON,
  };
};
