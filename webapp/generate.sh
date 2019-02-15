#!/usr/bin/env bash

copy_file(){
    echo "Copying $1 to $2"
    cp $1 $2 -R
}
auto_gen_dir=./src/auto_generated/
# rm -r ${auto_gen_dir}
mkdir -p ${auto_gen_dir}

copy_file ../README.md ${auto_gen_dir}

echo "Done. Please run \`build_data.sh\` as well"
python3 ./copy_default_templates.py > ${auto_gen_dir}/templateData.js
python3 ./copy_readme_template_section.py > ${auto_gen_dir}/README_TEMPLATE_SECTION.md
python3 ./copy_ts_model_definition.py > ${auto_gen_dir}/qualityResultDefinition.js